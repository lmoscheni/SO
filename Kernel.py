'''
Created on Jul 7, 2013

@author: Leandro Moscheni ; Julian Skalic
'''
import threading
from Cola import *
from SchedulerPolicy import *
from misExceptions import *

class Kernel():
    '''
        Representacion del Kernel de un sistema operativo.
        Es la entidad encargada de crear procesos, e interactuar
        con el hardware.
    '''
    def __init__(self):
        self.interruptionHandler = None
        self.schedulerPolicy = FIFO()
        self.readyQueue = Queue()
        self.nextPID = 0
      
    def setInterruptionHandler(self,intrHandler):
        self.interruptionHandler = intrHandler
        
    def searchProgramInDiskAndLoadInMemory(self,nameProgram):
        program = self.interruptionHandler.requestTheProgramDisk(nameProgram)
        self.interruptionHandler.requestMemorySpaceToLoadData(program,self.nextPID)
        pcb = self.interruptionHandler.requestNewProcessFromPageTable(self.nextPID)
        self.increaseNextPID()
        return pcb

    def createProcess(self,nameProgram):
        try:
            self.interruptionHandler.CPU.sleep(5)
            pcb = self.searchProgramInDiskAndLoadInMemory(nameProgram)
            self.readyQueue.add(pcb) 
            if(self.interruptionHandler.CPU.currentProcess == None) : self.interruptionHandler.CPU.currentProcess = pcb
        except (ExceptionNoProgramInDisk,ExceptionNoMemory), e:
            print e

    def increaseNextPID(self):
        self.nextPID = self.nextPID + 1

    def deleteProcess(self,process):
        self.readyQueue.remove(process)

    def FIFOPolicy(self):
        self.schedulerPolicy = FIFO()
        self.interruptionHandler.setQuantum(1000)

    def RRPolicy(self,q):
        self.schedulerPolicy = RoundRobin(q)
        self.interruptionHandler.setQuantum(self.schedulerPolicy.quantum)

    def PriorityPolicy(self):
        self.interruptionHandler.setQuantum(1)
        self.schedulerPolicy = Priority()

    def nextProcess(self):
        if self.readyQueue.isEmpty():
            return None
        else:
            return self.schedulerPolicy.getProcess(self.readyQueue)