import os
import shutil

# Function to move files based on their extensions
def organize_files(path):
    # Get all files in the directory
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    for file in files:
        # Skip hidden files (like .DS_Store)
        if file.startswith('.'):
            continue

        # Split the filename and extension
        filename, extension = os.path.splitext(file)
        # Remove the dot from the extension
        extension = extension[1:].lower()

        # Create the directory for the extension if it doesn't exist
        target_dir = os.path.join(path, extension)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # Move the file to the target directory
        try:
            shutil.move(os.path.join(path, file), os.path.join(target_dir, file))
            print(f"Moved {file} to {target_dir}")
        except Exception as e:
            print(f"Failed to move {file}: {e}")

# Prompt user for the directory path
path = os.path.expanduser(input('Enter desired path:'))

# Validate the input path
if not os.path.isdir(path):
    print("Invalid directory path. Please try again.")
else:
    organize_files(path)
