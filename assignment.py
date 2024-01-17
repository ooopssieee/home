from pathlib import Path
import os
import shutil
class Assignment:
    def __init__(self):
        pass

    def findDir(self,directory):
        if not directory.is_dir():
            print("Directory does not exist.\n")
            return False
        print("Directory exists.\n")
        return True
            
    def createDir(self,dir):
        assignmentDir=Path(f"/home/hx88xn/Documents/{dir}")
        isCreated=self.findDir(assignmentDir)
        if(not isCreated):
            os.mkdir(assignmentDir)
            print("Directory created.")
            return

    def createFile(self,dir):
        assignmentDir=Path(f"/home/hx88xn/Documents/{dir}")
        isDir=self.findDir(assignmentDir)
        if(isDir):
            fname=input("Name the assignment: ")
            file=open(f"{assignmentDir}/{fname}.docx","x")
            file.write("Test")
            print("Written to file.")
            file.close()
    
    def removeDir(self,dir):
        assignmentDir=Path(f"/home/hx88xn/Documents/{dir}")
        isDir=self.findDir(assignmentDir)
        if(not isDir):
            return
        shutil.rmtree(assignmentDir)
        print("Directory deleted.")
        
    def removeFile(self,dir,fname):
        assignment=Path(f"/home/hx88xn/Documents/{dir}/{fname}.docx")
        assdir=Path(f"/home/hx88xn/Documents/{dir}")
        if assignment.is_file() and assdir.is_dir():
            os.remove(assignment)
            print("Assignment removed.")
            return
        print("Does not exist.\n")