'''
Created on Jul 7, 2013

@author: Leandro Moscheni ; Julia Skalic
'''
import threading
import time

class CPU(threading.Thread):
    '''
        Entidad fisica encargada de correr las intrucciones, y computar
        intrucciones de calculo y logica.
    '''
    def __init__(self,memory,kernel,quantum):
        self.currentProces = None
        self.end = False
        self.kernel = kernel
        self.memory = memory
        self.clock = Clock(1)
        self.timmer = Timmer(quantum)
        self.run()
        
    def shutDown(self):
        self.end = True
        
    def loadProces(self,proces):
        self.timmer.reset()
        self.currentProces = proces
        
    def changeKernelMode(self):
        self.sleep(3)
        
    def getCurrentProces(self):
        return self.currentProces
    
    def isTimeOut(self):
        return self.timmer.isTheLimitOfCycles()
            
    def isEndProgram(self):
        return self.currentProces.reachedTheEnd()
        
    def runIntruction(self):
        self.memory.get(self.currentProces.getPC()).runInstruction()
        self.currentProces.increasePC()
        self.timmer.addCylce()

    def run(self):
        while True:
            self.runIntruction()
            if self.isTimeOut(): self.loadProces(self.kernel.getProces())
            if self.isEndProgram(): print "" # mandarInterrupcion
            if self.end: break
            
        
class Clock():
    '''
        Clase que representa al Reloj bajo el que corre la CPU.
        Basicamente es un temporizador, cuyo tiempo de estado 
        alto esta dado por la variable "window" que representa
        el tiempo en que dura la ventana abiera:
             _   _   _
        ck _| |_| |_| |_
             ^
             |
             window
        Al ser unas señal simetrica, el tiempo de estado bajo
        es igual al tiempo de estado alto, osea que la CPU
        tiene un tiempo de trabajo de "window" y un tiempo de
        descanso de "window" antes de reanudar al trabajo
    '''
    def __init__(self,window):
        self.window = window
        
    def run(self):
        return self.sleep()
    
    def sleep(self):
        time.sleep(self.window)
        
class Timmer():
    '''
        Entidad que tiene la labor de controlar la cantidad de ciclos de 
        CPU que se corren, basicamente su creacion se basa en la necesidad
        de contar los ciclos para la aplicacion del algoritmo RR de Scheduling
    '''
    def __init__(self,q):
        self.cyclesRun = 0
        self.quantum = q
        
    def reset(self):
        self.cyclesRun = 0
        
    def addCylce(self):
        self.cyclesRun = self.cyclesRun + 1
        
    def changeQuantum(self,q):
        self.quantum = q
    
    def isTheLimitOfCycles(self):
        return (self.cyclesRun == self.quantum)        