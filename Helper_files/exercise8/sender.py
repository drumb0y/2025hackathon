# correct answer is "Waffles"

import random
import time
import os
#from modules.customPrinter import rotatingPrintStringInSingleLine

SoutionTableArray = []

secretString = "Type \"Waffles\" to procede !"


def createTable():
    letters = 26
    print('File name :    ', os.path.abspath(__file__))
    print('Directory Name:     ', os.path.dirname(__file__))


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

#def printRotating():
   # rotatingPrintStringInSingleLine(getEncryptedString(secretString),50,500)
    
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
    
    #printRotating()
    
    time.sleep(5)
    
    startPrinting()




def getNumberInAlphabet(): # rather than having to account for uppercase and lowercase letters, convert all letters to lowercase
    
    stillRunning = True

    
    while (stillRunning):
        Char = secretString[positionCounter%len(secretString)]
        
        specialChar = chr(ord(Char)+ 35)
        
        
        print(specialChar, end="")
        positionCounter = positionCounter +1
    