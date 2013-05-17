"""
    uthor: Julian Skalick ; Leandro Moscheni.
    date: ...
    title: Timmer
"""

"""
    Representation of the physical device manager indicate 
    the number of instructions executed per cycle, so as to 
    establish the Quantum CPU each process.
"""
class Timmer():

    def __init__(self, valueRenovation):
        self.cycles = 0
        self.valueRenovation = valueRenovation

    def reset(self):
        self.cycles = 0

    def addCiclo(self):
        self.cycles = self.cycles + 1

    def quantumChange(self, q):
        self.valueRenovation = q
