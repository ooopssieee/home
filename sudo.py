from getpass import getpass
class Sudo:
    def __init__(self):
        self.login=False
    
    def readPassword(self):
        f=open("/home/hx88xn/Documents/hs.txt","r")
        return f.read()

    def changePassword(self,val):
        f=open("/home/hx88xn/Documents/hs.txt","w")
        f.write(val)
        f.close()

    def comparePw(self,val):
        pw=self.readPassword().strip()
        if val == pw:
            self.login=True
            c=input("\n-> ")
            match c:
                case "cp":
                    pw=getpass("\nENTER NEW PASSWORD: ")
                    self.changePassword(pw)
            return
        print("Password incorrect.")