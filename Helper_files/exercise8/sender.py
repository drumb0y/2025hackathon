# correct answer is "Waffles"

import random
import time
import os
import customPrinter as printer

SoutionTableArray = []

secretString = "Type \"Waffles\" to procede !"


def createTable():
    letters = 26


    print(os.path.dirname)
    
    tableFile = open(os.path.dirname(__file__) + "/SolutionTable.txt","w")
    
    while(letters > 0) :
        
        SoutionTableArray.insert(random.randint(0,len(SoutionTableArray)), chr(letters + 96))
        letters = letters -1
        
    
    for x in range(26):
        tableFile.write(SoutionTableArray[x])
        
    tableFile.close()    
    
def getEncryptedString(baseString):
    encryptedString = ""
    
    
    for c in baseString:
        
        if c in SoutionTableArray:
            specialChar = SoutionTableArray[ord(c)-96]
        else:
            specialChar = c
            
        encryptedString = encryptedString + specialChar
        
    return encryptedString

def printRotating():
    encString = getEncryptedString(secretString)
    print("printed ecrypted string " + encString)
    
    printer.rotatingPrintStringInSingleLine(encString,100,500)
    
    
    contentsOfFile = ""
    
    for i in range(0,random.randint(3,100)):
        contentsOfFile = contentsOfFile + encString
    print("\nfile content should be: " + contentsOfFile)    
    
    ListenFile = open(os.path.dirname(__file__) + "\ResultsFromListening.txt","w")
    ListenFile.write(contentsOfFile[random.randint(0,len(encString)):])
    ListenFile.close()
    
def startPrinting():
    stillRunning = True
    
    positionCounter = 0
        
    while (stillRunning):
        Char = secretString[positionCounter%len(secretString)]
        
        #print("char is: " + chr(ord(Char)))
        
        if Char in SoutionTableArray:
            specialChar = SoutionTableArray[ord(Char)-96]
        else:
            specialChar = Char

        print(specialChar, end="")
        positionCounter = positionCounter +1
    

## dont use
# def startPrinting():
# simple ceaser cipher
    
#     stillRunning = True
    
#     secretString = "Type \"Waffles\" to procede !"
#     positionCounter = 0
        
#     while (stillRunning):
#         Char = secretString[positionCounter%len(secretString)]
        
#         specialChar = chr(ord(Char)+ 35)
        
        
#         print(specialChar, end="")
#         positionCounter = positionCounter +1


if __name__ == "__main__":
    
    print('Get current working directory : ', os.getcwd())

    createTable()
    print(SoutionTableArray)
    
    printRotating()
    
    time.sleep(5)
    
    # startPrinting()




def getNumberInAlphabet(): # rather than having to account for uppercase and lowercase letters, convert all letters to lowercase
    
    stillRunning = True

    
    while (stillRunning):
        Char = secretString[positionCounter%len(secretString)]
        
        specialChar = chr(ord(Char)+ 35)
        
        
        print(specialChar, end="")
        positionCounter = positionCounter +1
    