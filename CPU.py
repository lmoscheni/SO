'''
Created on Jul 7, 2013

@author: Leandro Moscheni ; Julian Skalic
'''
import threading
import time

class CPU():
    '''
        Entidad fisica encargada de correr las intrucciones, y computar
        intrucciones de calculo y logica.
    '''
    def __init__(self):
        self.currentProcess = None
        self.end = False
        self.clock = Clock(3)
        self.timmer = Timmer(1)
        self.interruptionHandler = None
        
    def setInterruptionHandler(self,intrHandler):
        self.interruptionHandler = intrHandler

    def shutDown(self):
        self.end = True

    def getCurrentProcess(self):
        return self.currentProcess

    def loadProcess(self,process):
        self.timmer.reset()
        self.currentProcess = process
        if (process != None): process.setState("Running")

    def currentProcessRunning(self):
        return (self.currentProcess != None)

    def isTimeOut(self):
        return self.timmer.isTheLimitOfCycles()

    def isEndProgram(self):
        return self.currentProcess.reachedTheEnd()

    def runInstructionOfProcess(self):
        instruction = self.interruptionHandler.getInstruction(self.currentProcess.getPC() + self.currentProcess.getInicio())
        instruction.runInstruction()
        self.currentProcess.increasePC()
        self.timmer.addCylce()

    def checkStatusOfCurrentProcess(self):
        if self.isEndProgram() : return self.interruptionHandler.notifyTheKernelOfTerminationOfProcess
        if self.isTimeOut() : return self.interruptionHandler.notifyTheKernelOfContextSwitching

    def sleep(self,t):
        time.sleep(t)

    def run(self):
        while True:
            self.clock.run()
            if (self.currentProcess != None):
                self.runInstructionOfProcess()
                if self.isEndProgram(): self.interruptionHandler.notifyTheKernelOfTerminationOfProcess()
                else:
                    if self.isTimeOut(): self.interruptionHandler.notifyTheKernelOfContextSwitching()
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
        Al ser unas senal simetrica, el tiempo de estado bajo
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
