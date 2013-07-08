'''
Created on Jul 7, 2013

@author: Leandro Moscheni ; Julian Skalic
'''

class PCB():
    '''
        Clase que representa a un Bloque de Proceso, que en si es la modelizacion
        de un proceso en maquina.
    '''


    def __init__(self,pid,pc,fin,priority):
        self.PID = pid
        self.pc = pc
        self.inicio = pc
        self.fin = fin
        self.state = "Ready"
        self.priority = priority
        
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
