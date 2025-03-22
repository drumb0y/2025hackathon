import sys
import os
from Helper_files.lib import file_to_list, ensure_file_exists,exercise1,exercise2

def main():
    count = 0 
    if(ensure_file_exists("answers.txt")):
        print("Welcome to the Digital Scavenger Hunt! A new file was just created called answers.txt. You can see the contents of it using the command 'cat' and then the file name.\nTry it and rerun this program!")
    else:
        user_answers = file_to_list("answers.txt")
        answer_key = file_to_list("Helper_files/answer_key.txt")
        if user_answers == []:
            ensure_file_exists("one.txt")
            print("Awesome! Now the real fun begins. Let's get started with the basics. A new file was just created. Enter the name of the file (without the file type) in the first line of answers.txt")
            sys.exit()
        if user_answers[count] == answer_key[0]:
            print("Awesome now on to the next challenge")
            exercise1()
            count+=1
        if user_answers[count] != answer_key[0]:
            print("uh oh")
        if user_answers[count] == answer_key[1]:
            print("Awesome now on to the next challenge")
            exercise2()
        if user_answers[count] != answer_key[1]:
            print("uh oh")

if __name__ == "__main__":
    main()
