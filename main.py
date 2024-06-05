from flask import Flask, request, render_template, jsonify, send_from_directory
import os
import subprocess

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'  # Ensure this folder exists
app.config['RESULT_FOLDER'] = 'results/'  # Ensure this folder exists


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/oldsix-prompt')
def oldsix_prompt():
    return render_template('oldsix-prompt.html')


@app.route('/civitai')
def civitai():
    return render_template('civitai.html')


@app.route('/lora-trainer')
def lora_trainer():
    return render_template('lora_trainer.html')


@app.route('/run_lora_trainer', methods=['POST'])
def run_lora_trainer():
    try:
        result = subprocess.run(['python', 'lora_trainer.py'], capture_output=True, text=True, check=True)
        return jsonify({'output': result.stdout, 'error': result.stderr})
    except subprocess.CalledProcessError as e:
        return jsonify({'output': e.stdout, 'error': e.stderr}), 500


@app.route('/dreambooth')
def dreambooth():
    return render_template('dreambooth.html')


@app.route('/textual-inversion')
def textual_inversion():
    return render_template('textual-inversion.html')


@app.route('/canny-tryout')
def canny_tryout():
    return render_template('canny_tryout.html')

@app.route('/openpose-tryout')
def openpose_tryout():
    return render_template('openpose_tryout.html')


@app.route('/upload-images', methods=['POST'])
def upload_images():
    if 'image1' not in request.files or 'image2' not in request.files:
        return jsonify({'success': False, 'error': 'No file part'})

    image1 = request.files['image1']
    image2 = request.files['image2']

    if image1.filename == '' or image2.filename == '':
        return jsonify({'success': False, 'error': 'No selected file'})

    image1_path = os.path.join(app.config['UPLOAD_FOLDER'], 'image1.png')
    image2_path = os.path.join(app.config['UPLOAD_FOLDER'], 'image2.png')
    image1.save(image1_path)
    image2.save(image2_path)

    return jsonify({'success': True, 'image1_path': image1_path, 'image2_path': image2_path})


@app.route('/run_canny_tryout', methods=['POST'])
def run_canny_tryout():
    try:
        data = request.get_json()
        image1_path = os.path.join(app.config['UPLOAD_FOLDER'], 'image1.png')
        image2_path = os.path.join(app.config['UPLOAD_FOLDER'], 'image2.png')
        result_image1_path = os.path.join(app.config['RESULT_FOLDER'], 'result_image1.png')
        result_image2_path = os.path.join(app.config['RESULT_FOLDER'], 'result_image2.png')
        low_threshold = data['low_threshold']
        high_threshold = data['high_threshold']

        result = subprocess.run(
            ['python', 'canny_tryout.py', image1_path, image2_path, result_image1_path, result_image2_path,
             str(low_threshold), str(high_threshold)], capture_output=True, text=True, check=True)

        return jsonify({'success': True, 'result_url1': f'/results/{os.path.basename(result_image1_path)}',
                        'result_url2': f'/results/{os.path.basename(result_image2_path)}', 'output': result.stdout,
                        'error': result.stderr})
    except subprocess.CalledProcessError as e:
        return jsonify({'success': False, 'output': e.stdout, 'error': e.stderr})


@app.route('/results/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['RESULT_FOLDER'], filename)


if __name__ == "__main__":
    app.run(debug=True)
