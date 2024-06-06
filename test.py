import os
import shutil
import pandas as pd

# Define paths
csv_file_path = 'images.csv'          # Path to your CSV file
images_dir = 'images_original'        # Directory containing the original images
output_dir = 'sorted_images'          # Directory to save the sorted images
updated_csv_file_path = 'updated_images.csv'  # Path to save the updated CSV file

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Print the column names and the first few rows of the CSV file to verify
print("Column names:", df.columns)
print(df.head())

# Check and handle file extensions
def ensure_extension(filename):
    if not os.path.splitext(filename)[1]:
        return filename + '.jpg'  # Default to .jpg; adjust as needed
    return filename

# Assuming the columns are 'filename' and 'label'
for index, row in df.iterrows():
    image_name = row['image']  # Update based on actual column name
    image_name = ensure_extension(image_name)
    label = row['label']          # Update based on actual column name

    # Create label directory if it doesn't exist
    label_dir = os.path.join(output_dir, label)
    if not os.path.exists(label_dir):
        os.makedirs(label_dir)

    # Define source and destination paths
    src_path = os.path.join(images_dir, image_name)
    dst_path = os.path.join(label_dir, image_name)

    # Move the image to the corresponding label directory
    if os.path.exists(src_path):
        shutil.move(src_path, dst_path)
        print(f"Moved {src_path} to {dst_path}")
    else:
        print(f"File {src_path} does not exist. Full path attempted: {src_path}")

print("Images have been sorted and moved.")

# Rename images in the sorted directories and update CSV
updated_rows = []

for label in os.listdir(output_dir):
    label_dir = os.path.join(output_dir, label)
    if os.path.isdir(label_dir):
        for index, image_name in enumerate(os.listdir(label_dir), start=1):
            # Define the original file path
            original_file_path = os.path.join(label_dir, image_name)
            # Define the new file name and path
            new_file_name = f"{label}.{index}.jpg"
            new_file_path = os.path.join(label_dir, new_file_name)
            # Rename the file
            os.rename(original_file_path, new_file_path)
            print(f"Renamed {original_file_path} to {new_file_path}")
            # Update the CSV row
            updated_rows.append({'filename': new_file_name, 'label': label})

# Create a new DataFrame with updated rows and save to CSV
updated_df = pd.DataFrame(updated_rows)
updated_df.to_csv(updated_csv_file_path, index=False)

print(f"Images have been renamed and the CSV file has been updated. Updated CSV saved to {updated_csv_file_path}.")
