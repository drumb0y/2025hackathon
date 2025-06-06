# correct answer is "Waffles"

SoutionTableArray = []


def readTable():    

    tableFile = open("SolutionTable.txt","r")
    tableString = tableFile.read()
    
    for s in tableString:
        SoutionTableArray.append(s)

    tableFile.close()    
    

def deconvert():
    
    inputString = input("What is the string you would like decode")
    positionCounter = 0
    shift = input("what number would you like to shift by")
    
    outputstring = ""
    
    for s in inputString:
        if s in SoutionTableArray:
            indexOfEntry = SoutionTableArray.index(s)
            outputstring = outputstring + chr(indexOfEntry+96)
        else:
            outputstring = outputstring + s
            
    print(outputstring)
        
        
        
    # while (positionCounter < len(inputString)):
    #     Char = inputString[positionCounter]
        
    #     specialChar = chr(ord(Char)- int(shift))
        
        
    #     print(specialChar, end="")
    #     positionCounter = positionCounter +1



if __name__ == "__main__":
    readTable()
    print(SoutionTableArray)
    
    deconvert()
