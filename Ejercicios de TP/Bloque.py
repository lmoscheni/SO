class Bloque():
    def __init__(self,registroBase,registroLimite,instrucciones):
        self.registroBase = registroBase
        self.registroLimite = registroLimite
        #self.proximoBloque = proximoBloque
        self.listaDeInstrucciones = instrucciones
        #self.bloqueLibre = bloqueLibre

    def getProximoBloque(self):
        return self.proximoBloque

    def setProximoBloque(self,bloque):
        self.proximoBloque = bloque

    def esUltimoBloque(self):
        if self.proximoBloque == None:
            return True
        else:
            return False

    def esBloqueLibre(self):
        return self.bloqueLibre

    def espacioEnBloque(self):
        return (self.registroLimite - self.registroBase)

    def getRegistroBase(self):
        return self.registroBase

    def getRegistroLimite(self):
        return self.registroLimite

    def setRegistroBase(self,registro):
        self.registroBase = registro

    def setRegistroLimite(self,registro):
        self.registroLimite = registro

    def posicionEstaDentroDeHueco(self,pos):
        if pos >= self.registroBase & pos <= self.registroLimite:
            return True
        else:
            return False

    def leerInstruccion(self,pos):
        return self.listaDeInstrucciones[self.registroBase + pos]

    def terminoLecturaDeBloque(self,pos):
        retorno = False
        if pos == self.registroLimite:
            retorno = True
        return retorno

class BloqueLibre(Bloque):
    def __init__(self,registroBase,registroLimite,instr):
        Bloque.__init__(self,registroBase,registroLimite,instr,True)



class BloqueOcupado(Bloque):
    def __init__(self,registroBase,registroLimite,instr,proxBloque):
        Bloque.__init__(self,registroBase,registroLimite,instr,proxBloque,False)
