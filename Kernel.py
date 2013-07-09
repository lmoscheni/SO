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
    def __init__(self,intrHandler):
        self.interruptionHandler = intrHandler
        self.schedulerPolicy = None
        self.readyQueue = Queue()
        self.nextPID = 0
        
    def createProcess(self,pcb):
        self.increaseNextPID()
        self.readyQueue.add(pcb)
        
    def increaseNextPID(self):
        self.nextPID = self.nextPID + 1
        
    def deleteProcess(self,pcb):
        self.memory.free(pcb.getStart(),pcb.getEnd())
        self.readyQueue.remove(pcb)
        
    def FIFOPolicy(self):
        self.schedulerPolicy = FIFO()
        
    def RRPolicy(self):
        self.schedulerPolicy = RoundRobin()
        
    def PriorityPolicy(self):
        self.schedulerPolicy = Priority()
        
    def nextProcess(self):
        return self.schedulerPolicy.getProcess(self.readyQueue)