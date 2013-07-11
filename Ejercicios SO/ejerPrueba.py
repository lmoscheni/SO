import colaFifo
import Memoria
import kernel
import instruccion
import PCB
from time import sleep
import threading


class Main(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.queue = None

    def excecute(self,pcb):
        self.queue.setElement(pcb)

    def run(self):
        lisInstr = []
        inst1 = instruccion.Instruccion("ejecutandoPCB1")
        inst2 = instruccion.Instruccion("ejecutandoPCB2")
        inst3 = instruccion.Instruccion("ejecutandoPCB3")
        lisInstr.append(inst1)
        lisInstr.append(inst1)
        lisInstr.append(inst1)
        lisInstr.append(inst1)
        lisInstr.append(inst1)
        lisInstr2 = []
        lisInstr2.append(inst2)
        lisInstr2.append(inst2)
        lisInstr2.append(inst2)
        lisInstr2.append(inst2)
        lisInstr3 = []
        lisInstr3.append(inst3)
        lisInstr3.append(inst3)
        self.queue = colaFifo.QueueFifo()
        memoria = Memoria.Memoria()
        memoria.loadMemory(lisInstr)
        memoria.loadMemory(lisInstr2)
        memoria.loadMemory(lisInstr3)
        #algoritmo = AlgoritmoScheduler.Fifo(self.queue)
        kernell = kernel.Kernel(memoria,self.queue)
        kernell.startUp()
        pcb1 = PCB.PCB(1,"estado",0,5)
        pcb2 = PCB.PCB(2,"estado",5,9)
        pcb3 = PCB.PCB(3,"estado",9,11)
        sleep(0.1)
        kernell.newProces(pcb1)
        sleep(0.2)
        kernell.newProces(pcb2)
        sleep(1)
        kernell.newProces(pcb3)

SO = Main()
SO.start()
