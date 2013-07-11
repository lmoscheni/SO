'''
Created on Jul 7, 2013

@author: Leandro Moscheni ; Julian Skalic
'''
from Dictionary import *
from Programs import *

class HardDisk():
    '''
        Representacion de un Disco Rigido, o Almacenamiento Secuendario
    '''
    def __init__(self):
        self.space = Dictionary()

    def search(self,nameProgram):
        return self.space.lookUp(nameProgram)

    def save(self,program):
        programName = program.name
        self.space.addToDictionary(programName, program)

    def delete(self,nameProgram):
        self.space.remove(nameProgram)

