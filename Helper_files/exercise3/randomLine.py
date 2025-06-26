import os
import random

def insert():
    if os.path.isfile("ABC.txt"):
        with open("ABC.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()        
        if "Write this statement in the file \n" in lines:
        # Generate a random line number between 300 and 1000
            random_line = random.randint(300, 1000)

            # Insert '75A8' at that line (pad if needed)
            while len(lines) < random_line:
                lines.append("\n")
            lines.insert(random_line, "75A8\n")

            # Add the line number as the first line
            lines.insert(0, f"{random_line}\n")

            # Write back to the file
            with open("ABC.txt", "w", encoding="utf-8") as file:
                file.writelines(lines)

            print(f"Inserted '75A8'")
        else:
            raise ValueError("The statement dose not exist")  
    else:
        raise FileExistsError("ABC.txt not found.")
