from Shell import*
# Importacion del Shell
import sys
#importacion de bilbioteca del sistema
from PyQt4 import* QtGui
# Importacion de libreria grafica

class CLI():

    def __init__(self,usr,pwd):
        self.shell = Shell(usr,pwd)

    def initializeCLI(self):
        c = "> "

        while True:
            keyBoardInput = raw_input(c)
            if (keyBoardInput == "exit"):
                break
            elif (keyBoardInput == "login")


