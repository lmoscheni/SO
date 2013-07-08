'''
Created on Jul 7, 2013

@author: Leandro Moscheni ; Julian Skalic
'''
import threading
from Queue import *
from SchedulerPolicy import *
from PCB import *

class Kernel(threading.Thread):
    '''
        Representacion del Kernel de un sistema operativo.
        Es la entidad encargada de crear procesos, e interactuar
        con el hardware.
    '''
    def __init__(self,memory,cpu,hd,intrHandler):
        self.memory = memory
        self.CPU = cpu
        self.hdd = hd
        self.interruptionHandler = intrHandler
        self.schedulerPolicy = None
        self.readyQueue = Queue()
        self.nextPID = 0
        
    def createProcess(self,program):
        self.interruptionHandler.changeToKernelMode()
        process = self.hdd.search(program)
        result = self.memory.load(process)
        pcb = PCB(self.nextPID,result.getPC(),result.getFin())
        self.increaseNextPID()
        self.readyQueue.add(pcb)
        
    def increaseNextPID(self):
        self.nextPID = self.nextPID + 1
        
    def deleteProcess(self,p):
        self.memory.free(p.getStart(),p.getEnd())
        self.readyQueue.remove(p)
        
    def FIFOPolicy(self):
        self.schedulerPolicy = FIFO()
        
    def RRPolicy(self):
        self.schedulerPolicy = RoundRobin()
        
    def PriorityPolicy(self):
        self.schedulerPolicy = Priority()
        
    def nextProcess(self):
        return self.schedulerPolicy.getProcess(self.readyQueue)
