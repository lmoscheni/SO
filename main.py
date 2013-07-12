'''
Created on Jul 12, 2013

@author: leandro
'''
from CPU import *
from HardDisk import *
from IOSystem import *
from Memoria2 import *
from Instructions import *
from Programs import *
from PCB import *
from Kernel import *
from shell import *
from InterruptionHandler import *
from PageTable import * 

if __name__ == '__main__':
    #Definimos el programa 1
    program1 = Program("Gobstones","Ninguna")
    i1 = CPUInstruction("Poner")
    i2 = CPUInstruction("Mover")
    program1.addInstruction(i1)
    program1.addInstruction(i2)

    # Definimos el programa 2
    program2 = Program("programa.c","Ninguna")
    i3 = CPUInstruction("Main()")
    program2.addInstruction(i3)

    # Definimos un Disco
    hdd = HardDisk()
    hdd.save(program1)
    hdd.save(program2)

    # Definimos el Sistema de I/O
    iosys = IOSystem()
    iosys.addDevice(hdd)

    # Definimos la CPU con un quantum de 3
    cpu = CPU(3)

    # Definimos el Kernel
    kernel1point0 = Kernel()

    # Definimos la Memoria
    pageTable = PageTable()
    memory = Memoria(5,pageTable)

    # Definimos el Manejador de Interrupciones
    IH = InterruptionHandler(iosys,memory,pageTable,kernel1point0,cpu)

    # Seteamos el IH en todos los modulos que haga falta
    cpu.setInterruptionHandler(IH)
    kernel1point0.setInterruptionHandler(IH)
    kernel1point0.RRPolicy()

    # creamos el shell
    shell = Shell("123",IH)