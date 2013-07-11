class Block():
    def __init__(self,registroBase,registroLimite,instrucciones,pid):
        self.registroBase = registroBase
        self.registroLimite = registroLimite
        self.listaDeInstrucciones = instrucciones
        self.pidPCB = pid

    #Espacio del bloque
    def spaceOnBlock(self):
        return (self.registroLimite - self.registroBase)

    #Retorna el registro base del bloque
    def getBaseRegister(self):
        return self.registroBase

    #Retorna el registro limite del bloque
    def getLimitRegister(self):
        return self.registroLimite

    #Setea el registro base del bloque
    def setBaseRegister(self,register):
        self.registroBase = register

    #Setea el registro limite del bloque
    def setLimitRegister(self,register):
        self.registroLimite = register

    #Retorna el pid del pcb
    def getPID(self):
        return self.pidPCB

    #Verifica si la posicion pasada como parametro es la de ese bloque
    def positionInsideBlock(self,pos):
        if (pos >= self.registroBase) & (pos <= self.registroLimite):
            return True
        else:
            return False

    #Lee la isntruccion de la posicion
    def readInstruction(self,pos):
        return self.listaDeInstrucciones[pos - (self.registroBase)]

