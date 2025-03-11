    
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

def ensure_file_exists(filename,contents):
    created = False
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(contents)  # Create an empty file
        created = True
    return created

def ensure_folder_exists(foldername,files:list,contents:list ):
    created = False
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("")  # Create an empty file
        created = True
    return created