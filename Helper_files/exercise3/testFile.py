import os 
def check():
    if os.path.isfile("ABC.txt"):
        with open("ABC.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()        
        if "Write this statement in the file \n" in lines:
            num = int(lines[0])
            if (lines[num -1] is "0111 0101 1010 1000" )or (lines[num -1]=="0111010110101000"):
                print("Put this in the answer file: hqwlfjalfq65d")
            else:
                raise ValueError("binary not correct")
        else:
            raise ValueError("String not found in the file")
    else:
        raise FileNotFoundError()
check()