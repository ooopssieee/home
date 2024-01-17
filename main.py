from assignment import Assignment
from sudo import Sudo
from getpass import getpass
line="\n-------------------------------------------------------------\n"
menu=f"{line}\t\t\tH O M E\n\n c- Create Directory\n f- Create assignment\n r- Delete Directory\n d- Delete assignment\n q- Exit\n\n"
ass=Assignment()
run=1
while(run):
    choice=input(menu)
    match choice:
        case 'c':
            dir=input("Name your directory:\n")
            ass.createDir(dir)
        case 'f':
            dir=input("Directory:\n")
            ass.createFile(dir)
        case 'r':
            dir=input("Name the directory to:\n")
            ass.removeDir(dir)
        case 'd':
            dir=input("Name the directory:\n")
            fname=input("Assignment:\n")
            ass.removeFile(dir,fname)
        case 'q':
            run=0
        case "sudo":
            val=getpass("ENTER PASSWORD: ")
            s=Sudo()
            s.comparePw(val)
