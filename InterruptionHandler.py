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
    def __init__(self,kernel,cpu,ioSys,memory):
        self.CPU = cpu
        self.kernel = kernel
        self.ioSystem = ioSys
        self.memory = memory
    
    # Cambia al modo Kernel
    def changeToKernelMode(self):
        print ""

    def changeToNormalMode(self):
        print ""

    # Apaga la CPU    
    def shutDownPC(self):
        self.CPU.shutDown()
    
    # Notifica al Kernel de la finalizacion de un proceso, para que lo
    # quite de la cola de Ready    
    def notifyTheKernelOfTherminationOfProcess(self,pcb):
        self.requestToFreeMemorySpace(pcb)
        self.kernel.deleteProcess(pcb)
        self.notifyTheKernelOfContextSwitching()
    
    # Notifica al Kernel, de un cambio de contexto, para que este,actue
    # en consecuencia    
    def notifyTheKernelOfContextSwitching(self):
        self.CPU.loadProcess(self.kernel.nextProcess())
    
    # El Shell pide al Kernel, la creacion de un proceso, referente a un
    # programa alojado en disco.    
    def askTheKernelToCreateProcess(self,nameProgram):
        program = self.requestTheProgramDisk(nameProgram)
        pcb = self.requestMemorySpaceToLoadData(program)
        self.kernel.addProcess(pcb)
    
    # El kernel pide a memoria principal, espacio para cargar a un programa,
    # de haber espacio, se pasa a la carga del programa en memoria, caso
    # contrario se levanta una excepcion    
    def requestMemorySpaceToLoadData(self,program):
        pcb = self.memory.load(program)
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