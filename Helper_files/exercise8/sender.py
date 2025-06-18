# correct answer is "Waffles"

import random
import os

SoutionTableArray = []

def createTable():
    letters = 26
    
    tableFile = open(os.getcwd() + "\SolutionTable.txt","w")
    
    while(letters > 0) :
        
        SoutionTableArray.insert(random.randint(0,len(SoutionTableArray)), chr(letters + 96))
        letters = letters -1
        
    
    for x in range(26):
        tableFile.write(SoutionTableArray[x])
        
    tableFile.close()    
    
    
def startPrinting():
    stillRunning = True
    
    secretString = "Type \"Waffles\" to procede !"
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
    

# def startPrinting():
    
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
    
    # startPrinting()


def getNumberInAlphabet(): # rather than having to account for uppercase and lowercase letters, convert all letters to lowercase
    
    stillRunning = True

    
    while (stillRunning):
        Char = secretString[positionCounter%len(secretString)]
        
        specialChar = chr(ord(Char)+ 35)
        
        
        print(specialChar, end="")
        positionCounter = positionCounter +1
    