<b> Combination of Classification and Stable Diffusion </b></p>
This project combines image classification with stable diffusion using a Colab environment. It includes uploading a picture, classifying it with a pre-trained model, and generating related images using stable diffusion.

<b>Here is the link : https://colab.research.google.com/drive/1OemVMn-CMT3isCRJrB8qZl83hhL7CBhl</b>
<p><b>Dataset for cloth classification: https://www.kaggle.com/datasets/agrigorev/clothing-dataset-full</b></p>

<b> Table of Contents </b></p>
1. Introduction </p>
2. Features</p>
3. Technologies Used</p>
4. Installation</p>
5. Usage</p>
6. Project Structure</p>
7. Contributors</p>
8. License</p>

<b>1. Introduction</b> <p>
This project investigates the potential of Artificial Intelligence Generated Content (AIGC) in fashion style layouts, driven by the growing need for tools that enable designers to incorporate diverse visual elements into their work—leveraging state-of-the-art text-to-image technologies and ControlNet, aiming to solve the challenge of integrating 3D material fashion as complementary control data within solid diffusion models. The project develops a stable diffusion management community version tailored explicitly to fashion design, allowing for creation unique patterns and textures on fabric. Preliminary results indicate that this approach can significantly enhance the creative process, offering fashion enterprises a practical and scalable solution. It will focus on refining the model and expanding its application across broader style design contexts.

<b>2. Features </b></p>
1. Upload images and classify them using a pre-trained neural network.
2. Generate related images using stable diffusion based on classification results.
3. Simple and easy-to-use interface on Google Colab.

<b>3.  Technologies Used </b></p>
1. Python
2. PyTorch
3. Torchvision
4. Google Colab
5. Stable Diffusion

<b>4.  Installation</b></p>
To run this project, follow these steps:</p>
1. Clone the repository:</p>
git clone https://github.com/yourusername/yourproject.git

2. Navigate to the project directory:</p>
cd your project

3. Open the Jupyter Notebook in Google Colab:</p>
Upload the notebook Combination_of_classify_n_callingstablediffusion.ipynb to your Google Drive.

4. Open it with Google Colab.</p>

5. Install the required dependencies: </p>
pip install torch torchvision


<b>5. Usage</b></p>
1. Open the notebook in Google Colab. </p>
2. Follow the steps outlined in the notebook:</p>
    - Upload the image.</p>
    - Run the classification model on the uploaded image.</p>
    - Generate related images using stable diffusion.</p>

6. Project Structure</p>
This flowchart represents a structured process for implementing a Virtual Try-On System using Artificial Intelligence-Generated Content (AIGC) technology, specifically through the Stable Diffusion model and ControlNet. The objective is to seamlessly generate realistic images of clothing applied to a person’s image, allowing users to visualize how the clothing will look. 

The system is designed to simplify and automate the process of clothing image generation by combining machine learning for classification, ChatGPT for prompt generation, and Stable Diffusion for photorealistic image production. This flow enables beginners and professionals in the fashion industry to create high-quality visual content with minimal manual input.

 
(Figure 1: Flow Chart of Designing Virtual Try-On)


7. Contributors</p>
Ho Yin Ling</p>

8. License</p>
Specify the license under which your project is distributed. If you're unsure, you can use an open-source license like MIT.

This project is licensed under the MIT License - see the LICENSE file for details.
