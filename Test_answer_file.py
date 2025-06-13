import sys
import os
from Helper_files.exercise1 import exercise1  # Import exercise2 if you want to call it
from Helper_files.lib import ensure_file_exists, file_to_list  # Assuming these functions exist here
def main():
    count = 0 
    if(ensure_file_exists("answers.txt")):
        print("Welcome to the Digital Scavenger Hunt! A new file was just created called answers.txt. You can see the contents of it using the command 'cat' and then the file name.\nTry it and rerun this program!")
    else:
        user_answers =file_to_list("answers.txt")
        exercise1()
     

if __name__ == "__main__":
    main()
