'''
Created on Jul 7, 2013

@author: Leandro Moscheni ; Julian Skalic
'''

class InterruptionHandler():
    '''
        Entidad que almacena el comportamiento de todas las interrupciones
        del Sistema, y hacer interactuar a los participes entre dichas
        interrupciones
    '''
    def __init__(self,kernel,cpu):
        self.CPU = cpu
        self.kernel = kernel
    
    def changeToKernelMode(self):
        self.CPU.changeKernelMode()
        
    def shutDownPC(self):
        self.CPU.shutDown()
        
    def notifyTheKernelOfTherminationOfProcess(self,process):
        self.changeToKernelMode()
        self.kernel.deleteProcess(process)
        
    def notifyTheKernelOfContextSwitching(self):
        self.changeToKernelMode()
        self.CPU.loadProcess(self.kernel.nextProcess())