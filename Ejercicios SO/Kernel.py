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

    def createProcess(self,program):
        try:
            self.interruptionHandler.changeToKernelMode()
            program = self.interruptionHandler.requestTheProgramDisk(program)
            self.interruptionHandler.requestMemorySpaceToLoadData(program,self.nextPID)
            #baseRegister = self.interruptionHandler.requestBaseRegisterToPageTable(self.nextPID)
            #limitRegister = self.interruptionHandler.requestLimitRegisterToPageTable(self.nextPID)
            pcb = self.interruptionHandler.requestNewProcessFromPageTable(self.nextPID) #PCB(self.nextPID,baseRegister,limitRegister)
            if self.readyQueue.isEmpty() & (not self.interruptionHandler.requestRunningProcessOnCPU()): self.interruptionHandler.requestLoadProcesOnCPU(pcb)
            else: self.readyQueue.add(pcb)
            self.increaseNextPID()
        except (ExceptionNoProgramInDisk,ExceptionNoMemory), e:
            print e

    def increaseNextPID(self):
        self.nextPID = self.nextPID + 1

    def deleteProcess(self,p):
        self.interruptionHandler.requestToFreeMemorySpace(p)
        if (not self.readyQueue.isEmpty()):
            retorno = self.schedulerPolicy.getProcess(self.readyQueue)
            self.readyQueue.remove(retorno)
            self.interruptionHandler.requestLoadProcesOnCPU(retorno)
        else:
            self.interruptionHandler.requestLoadProcesOnCPU(None)
            #self.interruptionHandler.shutDownPC()

    def FIFOPolicy(self):
        self.schedulerPolicy = FIFO()

    def RRPolicy(self):
        self.schedulerPolicy = RoundRobin()

    def PriorityPolicy(self):
        self.schedulerPolicy = Priority()

    def nextProcess(self):
        CPUProcess = self.interruptionHandler.getCurrentProcessOnCPU()
        self.readyQueue.add(CPUProcess)
        retorno = self.schedulerPolicy.getProcess(self.readyQueue)
        self.readyQueue.remove(retorno)
        self.interruptionHandler.requestLoadProcesOnCPU(retorno)
