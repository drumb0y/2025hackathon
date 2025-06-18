import os 
import shutil

pathToBTSFiles = os.getcwd() # directory that has the all production files
pathToPlayerFiles = "" # can change as needed but this is the folder that we can add files to as a player levels up
currentLevel = 0 # counter to track player level
playerName = "TEST TEAM" # 


def start(): #start from here and create exercise 1
    pathToBTSFiles = os.getcwd() # get the directory of the production/BTS files
    os.system("cd ..")
    print
    
    
    print("Hello how are you doing, this sounds like a wonderful day\n")
    print("Secret says that the CS professors have locked their answerkeys for the midterm and finals behind all of these challenges\n")
    print("You have found the location of all the answerkeys, the data center in prothro, but unfortunatly \n")
    
    unlockLevel(8)
    


def unlockLevel(levelNumber) : # as the player leves up, 
    
    if levelNumber == 8:
        print("unlocking level 8")
        unlockLevel8()
        
        
        
def unlockLevel8() :
    os.system(("mkdir " + (pathToPlayerFiles+"exercise8")))
    
    moveFileFromAtoB(pathToBTSFiles+"\exercise8\Exercise8descrition.txt", pathToPlayerFiles+"\exercise8\Exercise8descrition.txt")

    
    
    
def moveFileFromAtoB(fileToBeMoved, endLocationFolder) :
    shutil.copyfile(fileToBeMoved, endLocationFolder)
    
    
if __name__ == "__main__":
    print(os.getcwd())
    unlockLevel(8)
