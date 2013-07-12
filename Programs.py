"""
    authors: Julian Skalick ; Leandro Moscheni.
    date: ...
    title: Programs
"""

# Class representing the concept of program as a sequence
# of low-level instructions.
class Program():

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.listOfInstructions = []

    def addInstruction(self, instr):
        self.listOfInstructions.append(instr)

    def name(self):
        return self.name

    def getInstructions(self):
        return self.listOfInstructions

    def runProgram(self):
        for instr in self.listOfInstructions:
            instr.runInstruction()


