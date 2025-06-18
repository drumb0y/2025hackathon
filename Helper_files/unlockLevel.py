import os 
import shutil

parentDir = os.path.dirname(os.getcwd()) # directory that both player and helper files are in
pathToBTSFiles = os.getcwd() # directory that has the all production files
pathToPlayerFiles = parentDir + "\playerfiles" # can change as needed but this is the folder that we can add files to as a player levels up
currentLevel = 0 # counter to track player level
playerName = "TEST TEAM" # 


def start(): #start from here and create exercise 1    
    
    print(parentDir)
    print(pathToBTSFiles)
    print(pathToPlayerFiles)
    
    ### intro to hackathon
    print("Hello how are you doing, this sounds like a wonderful day\n")
    print("Secret says that the CS professors have locked their answerkeys for the midterm and finals behind all of these challenges\n")
    print("You have found the location of all the answerkeys, the data center in prothro, but unfortunatly \n")
    
    unlockLevel(8)
    


def unlockLevel(levelNumber) : # as the player leves up, 
    print("unlocking level " + str(levelNumber))

    
    ## for each level, run the according command to copy the required files to the players folder
    if levelNumber == 1:
        unlockLevel1()
    elif levelNumber == 2:
        unlockLevel2()
    elif levelNumber == 3:
        unlockLevel3()
    elif levelNumber == 4:
        unlockLevel4()
    elif levelNumber == 5:
        unlockLevel5()
    elif levelNumber == 6:
        unlockLevel6()
    elif levelNumber == 7:
        unlockLevel7()
    elif levelNumber == 8:
        unlockLevel8()
        
        
        
        
def unlockLevel8() :
    os.system(("mkdir " + (pathToPlayerFiles+"\exercise8")))
    
    moveFileFromAtoB(pathToBTSFiles+"\exercise8\Exercise8descrition.txt", pathToPlayerFiles+"\exercise8\Exercise8descrition.txt")

    
def moveFileFromAtoB(fileToBeMoved, endLocationFolder) :
    shutil.copyfile(fileToBeMoved, endLocationFolder)
    
    
if __name__ == "__main__":
    print(os.getcwd())
    start()
    #unlockLevel(8)
