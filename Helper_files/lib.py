    
import os

def file_to_list(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Remove newline characters from each line
        lines = [line.strip() for line in lines]
        return lines
    except FileNotFoundError:
        print("Error: File not found.")
        return []

def ensure_file_exists(filename,contents=""):
    created = False
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(contents)  # Create a file with stuff in it
        created = True
    return created

def ensure_folder_exists(foldername, files_and_contents):
    created = False
    path = os.path.join(".", foldername)  # Ensure the folder is created inside the current directory
    if not os.path.exists(path):
        os.mkdir(path)
        for file, content in files_and_contents:
            file_path = os.path.join(path, file)  # Ensure the file is placed inside the folder
            ensure_file_exists(file_path, content)
        created = True
    return created

