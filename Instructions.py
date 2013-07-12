""" 
    authors: Julian Skalick ; Leandro Moscheni.
    date: ...
    title: Shell Exceptions
"""
# Class representing the concept of low-level instruction.
class Instruction():

    def __init__(self, name):
        self.name = name

    def runInstruction(self):
        print("The method is not defined.")

    def isIOInstruction(self):
        return(False)
    

# Class representing the concept of instruction that communicates 
# with devices I/O.
class IOInstruction(Instruction):

    def __init__(self, name):
        Instruction.__init__(self, name)
        
    def runInstruction(self):
        print "Ejecuto ",self.name

# Class representing the concept of instruction that takes place 
# entirely in the CPU
class CPUInstruction(Instruction):
    
    def __init__(self,name):
        Instruction.__init__(self, name)
    
    def runInstruction(self):
        print "Ejecuto ",self.name

