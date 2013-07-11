'''
Created on Jul 7, 2013

@author: Leandro Moscheni ; Julian Skalic
'''

class InterruptionHandler():
    '''
        Entidad que almacena el comportamiento de todas las interrupciones
        del Sistema, y hace interactuar a los participes entre dichas
        interrupciones.
    '''
    def __init__(self,ioSys,memory,pageTable):
        self.CPU = None
        self.kernel = None
        self.ioSystem = ioSys
        self.memory = memory
        self.pageTable = pageTable

    # Cambia al modo Kernel
    def changeToKernelMode(self):
        print ""

    def changeToNormalMode(self):
        print ""

    def setKernel(self,kernel):
        self.kernel = kernel

    def setCPU(self,CPU):
        self.CPU = CPU

    # Apaga la CPU
    def shutDownPC(self):
        self.CPU.shutDown()

    # Notifica al Kernel de la finalizacion de un proceso, para que lo
    # quite de la cola de Ready
    def notifyTheKernelOfTerminationOfProcess(self,pcb):
        self.requestToFreeMemorySpace(pcb)
        self.kernel.deleteProcess(pcb)
        self.notifyTheKernelOfContextSwitching()

    # Notifica al Kernel, de un cambio de contexto, para que este,actue
    # en consecuencia
    def notifyTheKernelOfContextSwitching(self):
        self.kernel.nextProcess()

    # El Shell pide al Kernel, la creacion de un proceso, referente a un
    # programa alojado en disco.
    def askTheKernelToCreateProcess(self,nameProgram):
        program = self.requestTheProgramDisk(nameProgram)
        pcb = self.requestMemorySpaceToLoadData(program)
        self.kernel.addProcess(pcb)

    # El kernel pide a memoria principal, espacio para cargar a un programa,
    # de haber espacio, se pasa a la carga del programa en memoria, caso
    # contrario se levanta una excepcion
    def requestMemorySpaceToLoadData(self,program, pidPCB):
        pcb = self.memory.load(pidPCB,program)
        return pcb

    # El kernel, pide al disco, que este le de un porgrama que se encuentra
    # alojado en el, en caso de no existir, levanta una excepcion
    def requestTheProgramDisk(self,nameProgram):
        program = self.ioSystem.search(nameProgram)
        return program

    # El kernel le pide a memoria, que libere el espacio, ocupado por determinado
    # proceso
    def requestToFreeMemorySpace(self,pcb):
        self.memory.free(pcb)

    # El InterruptionHandler pide a memoria la instruccion en la posicion base
    # (position)
    def requestInstructionForMemory(self,position):
        return self.memory.read(position)

    #El InterruptionHandler pide cargar al cpu un proceso para ejecutar
    def requestLoadProcesOnCPU(self,pcb):
        self.CPU.loadProcess(pcb)

    #El InterruptionHandler pide el proceso en CPU
    def getCurrentProcessOnCPU(self):
        process = self.CPU.getCurrentProcess()
        return process

    #El InterruptionHandler pregunta si hay un proceso corriendo en CPU
    def requestRunningProcessOnCPU(self):
        return self.CPU.currentProcessRunning()

    #Retorna un nuevo proceso que se cargo en memoria y en la tabla
    def requestNewProcessFromPageTable(self,pid):
        return self.pageTable.getPCB(pid)
