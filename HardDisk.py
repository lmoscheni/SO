'''
Created on Jul 7, 2013

@author: Leandro Moscheni ; Julian Skalic
'''
from Dictionary import *

class HardDisk():
    '''
        Representacion de un Disco Rigido, o Almacenamiento Secuendario
    '''
    def __init__(self):
        self.space = {}

    def search(self,nameProgram):
        return self.space[nameProgram]

    def save(self,program):
        self.space[program.name()] = program

    def delete(self,nameProgram):
        self.space.remove(nameProgram)

