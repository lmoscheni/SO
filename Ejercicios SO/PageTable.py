class PageTable():

    def __init__(self,memoria):
        self.listPCBs = [{}]
        self.memoria = memoria

    def agregarPCB(self,pcb,instr):
        self.listPCBs.append({"id":pcb.getPID(),"registroBase":base,"registroLimite":limite})

    def getRegistroBaseDe(self,id):
        retorno = None
        for elem in self.listPCBs:
            if elem["id"] == id:
                retorno = elem["registroBase"]
        return retorno

    def getRegistroLimiteDe(self,id):
        retorno = None
        for elem in self.listPCBs:
            if elem["id"] == id:
                retorno = elem["registroLimite"]
        return retorno

