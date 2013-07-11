'''
Created on Jul 7, 2013

@author: Leandro Moscheni ; Julian Skalic
'''

class PCB():
    '''
        Clase que representa a un Bloque de Proceso, que en si es la modelizacion
        de un proceso en maquina.
    '''


    def __init__(self,pid,base,limite):
        self.PID = pid
        self.pc = 0
        self.inicio = base
        self.fin = limite
        self.state = "Ready"
        self.priority = None

    def getPID(self):
        return self.PID

    def getPC(self):
        return self.pc

    def getInicio(self):
        return self.inicio

    def getFin(self):
        return self.fin

    def getState(self):
        return self.state

    def setState(self,value):
        self.state = value

    def getPriority(self):
        return self.priority

    def increasePC(self):
        self.pc = self.pc + 1

    def reachedTheEnd(self):
        return ((self.pc+self.inicio) > self.fin)
