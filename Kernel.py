'''
Created on Jul 7, 2013

@author: Leandro Moscheni ; Julian Skalic
'''
import threading
from Cola import *
from SchedulerPolicy import *
from Bloque import *
from misExceptions import *
from PCB import *

class Kernel(threading.Thread):
    '''
        Representacion del Kernel de un sistema operativo.
        Es la entidad encargada de crear procesos, e interactuar
        con el hardware.
    '''
    def __init__(self,intrHandler):
        self.interruptionHandler = intrHandler
        self.schedulerPolicy = FIFO()
        self.readyQueue = Queue()
        self.nextPID = 0
        
    def searchProgramInDiskAndLoadInMemory(self,nameProgram):
        program = self.interruptionHandler.requestTheProgramDisk(program)
        self.interruptionHandler.requestMemorySpaceToLoadData(program,self.nextPID)
        pcb = self.interruptionHandler.requestNewProcessFromPageTable(self.nextPID)
        self.increaseNextPID()
        return pcb

    def createProcess(self,nameProgram):
        try:
            self.interruptionHandler.changeToKernelMode()
            pcb = self.searchProgramInDiskAndLoadInMemory(nameProgram)
            self.readyQueue.add(pcb)
        except (ExceptionNoProgramInDisk,ExceptionNoMemory), e:
            self.interruptionHandler.sendShellMessage(e)

    def increaseNextPID(self):
        self.nextPID = self.nextPID + 1

    def deleteProcess(self,process):
        self.readyQueue.remove(process)

    def FIFOPolicy(self):
        self.schedulerPolicy = FIFO()

    def RRPolicy(self):
        self.schedulerPolicy = RoundRobin()

    def PriorityPolicy(self):
        self.schedulerPolicy = Priority()

    def nextProcess(self):
        if self.readyQueue.isEmpty():
            return None
        else:
            return self.schedulerPolicy.getProcess(self.readyQueue)