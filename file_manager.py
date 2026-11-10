import os
import shutil

# File extensions
audio = ['.mp3', '.wma', '.aac', '.wav', '.flac']
video = ['.mp4', '.wmv', '.avi', '.mkv', '.mov']
docs = ['.docx', '.pdf', '.txt', '.xlsx', '.pptx', '.csv']
software = ['.exe', '.apk', '.msi']
zips = ['.zip', '.rar', '.7z']

# Main directory
path = r"C:\Users\RISHABH\OneDrive\New folder (2)\Movie_Recommender_System"

# Destination folders
categories = ['audio', 'video', 'docs', 'software', 'zips', 'unknown']

# Create folders if they don't exist
for category in categories:
    os.makedirs(os.path.join(path, category), exist_ok=True)


# Function to move files
def move_file(source, extension):

    extension = extension.lower()

    if extension in audio:
        category = 'audio'
    elif extension in video:
        category = 'video'
    elif extension in docs:
        category = 'docs'
    elif extension in software:
        category = 'software'
    elif extension in zips:
        category = 'zips'
    else:
        category = 'unknown'

    destination = os.path.join(path, category)
    filename = os.path.basename(source)
    target = os.path.join(destination, filename)

    # Avoid overwriting existing files
    if os.path.exists(target):
        name, ext = os.path.splitext(filename)
        count = 1

        while os.path.exists(target):
            new_filename = f"{name}_{count}{ext}"
            target = os.path.join(destination, new_filename)
            count += 1

    shutil.move(source, target)
    print(f"Moved: {filename} -> {category}")


# Get directory contents
files = os.listdir(path)

for file in files:

    source = os.path.join(path, file)

    # Skip destination folders
    if file.lower() in categories and os.path.isdir(source):
        continue

    # If item is a directory
    if os.path.isdir(source):

        files1 = os.listdir(source)

        for file1 in files1:

            source1 = os.path.join(source, file1)

            # Handle files inside the directory
            if os.path.isfile(source1):

                extension = os.path.splitext(file1)[1]
                move_file(source1, extension)

            # Handle nested directories
            elif os.path.isdir(source1):
                print(f"Skipped nested folder: {file1}")

    # If item is a file
    elif os.path.isfile(source):

        extension = os.path.splitext(file)[1]
        move_file(source, extension)

print("\nFile organization completed!")
