import sys
import time

        
        
"""
print a given string on the same line while cycling througth the charecters in the string


stringToPrint - message that should be printed to the command line
numberOfCharectersOnScreen - number of charecters that can be displayed on the command line at a given moment
numOfCharsToBePrinted - how many total charecters to be printed to the command line

"""    
def rotatingPrintStringInSingleLine(stringToPrint, numOfCharsOnScreen, numOfCharsToBePrinted):
    fulllengthString = "" # create a string that contains multiple versions of the message to be printed so that the print statment can cycle througth the charecters in an efficent way
    
    print(int(numOfCharsToBePrinted/len(stringToPrint))+1)
    for i in range(0,int(numOfCharsToBePrinted/len(stringToPrint))+1):
        fulllengthString = fulllengthString + stringToPrint
        
    #print(fulllengthString)
    
    positionCounter = 0
    
    for i in range(0,(len(fulllengthString)-int(len(stringToPrint)))):
        sys.stdout.write("\r |" + fulllengthString[positionCounter:(positionCounter+numOfCharsOnScreen)] + "|")
        positionCounter = positionCounter +1
        time.sleep(.01)



     
    
    
if __name__ == "__main__":

    rotatingPrintStringInSingleLine("hello!", 100, 1000)


    # i = 100
    
    # while (True):
    #     i = i+1
    #     sys.stdout.write("\r " + str(i))
        
