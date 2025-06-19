def run2 ():
    with open("ridles.txt", "r", encoding="utf-8") as file:
        ridles = file.read()
    ensure_folder_exists ("exercise2",[
        ("Another_Problem.txt","Someone has lost access to a file they were editing. You have been tasked with restoring their permissions and then you have to finish their work\n "),
        ("uno_hell_tm_riddle.txt",ridles)]
        ,[0o766,0o000,0o000])