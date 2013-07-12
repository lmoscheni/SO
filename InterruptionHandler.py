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
    def __init__(self,ioSys,memory,pageTable,kernel,cpu):
        self.CPU = cpu
        self.kernel = kernel
        self.ioSystem = ioSys
        self.memory = memory
        self.pageTable = pageTable
        self.shell = None
        
    def setShell(self,anShell):
        self.shell = anShell

    # Cambia al modo Kernel
    def changeToKernelMode(self):
        self.kernel.run()
        self.CPU.wait()

    # Cambia al modo Normal de ejecucion
    def changeToNormalMode(self):
        self.kernel.wait()
        self.CPU.run()

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
        #self.changeToKernelMode()
        self.kernel.deleteProcess(pcb)
        self.notifyTheKernelOfContextSwitching()

    # Notifica al Kernel, de un cambio de contexto, para que este,actue
    # en consecuencia
    def notifyTheKernelOfContextSwitching(self):
        pcb = self.kernel.nextProcess()
        #self.changeToNormalMode()
        self.requestLoadProcessOnCPU(pcb)
        
    # El Shell pide al Kernel, la creacion de un proceso, referente a un
    # programa alojado en disco.
    def askTheKernelToCreateProcess(self,nameProgram):
        self.kernel.createProcess(nameProgram)
        
        #self.changeToNormalMode()

    # El kernel pide a memoria principal, espacio para cargar a un programa,
    # de haber espacio, se pasa a la carga del programa en memoria, caso
    # contrario se levanta una excepcion
    def requestMemorySpaceToLoadData(self,program, pidPCB):
        pcb = self.memory.load(pidPCB,program)
        return pcb

    # El kernel, pide al disco, que este le de un porgrama que se encuentra
    # alojado en el, en caso de no existir, levanta una excepcion
    def requestTheProgramDisk(self,nameProgram):
        program = self.ioSystem.getProgram(nameProgram)
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
    def requestLoadProcessOnCPU(self,pcb):
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

    # Se utiliza cuando el Kernel quiere notificar de algun suceso al usuario.
    def sendShellMessage(self,msj):
        self.shell.showMessageInTheDisplay(msj)
        
    # Se utiliza para pedir un proceso en caso de que no haya ninguno en CPU    
    def getNewProcess(self):
        #self.changeToKernelMode()
        pcb = self.kernel.nextProcess()
        self.requestLoadProcessOnCPU(pcb)
    
    # Retorna la instruccion que se encuenta en la posicion "position"    
    def getInstruction(self, position):
        instruction = self.memory.read(position)
        return instruction
    
    # Permite al algoritmo RR cambiar un Quantum
    def setQuantum(self,q):
        self.CPU.timmer.changeQuantum(q)
        
    # Hace Seleccion FIFO sobre la cola de listos
    def FIFOQueue(self):
        self.kernel.FIFOPolicy()
        
    # Hace Seleccion RR sobre la cola de listos
    def RRQueue(self,q):
        self.kernel.RRPolicy(q)
        
    def PriorityPolicy(self):
        self.kernel.PriorityPolicy()