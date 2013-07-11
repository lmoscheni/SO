from Memoria2 import *

class PageTable():

    def __init__(self):
        self.listPCBs = []

    def agregarPCB(self,pid,base,limite):
        self.listPCBs.append({"id":pid,"registroBase":base,"registroLimite":limite})

    def getRegistroBaseDe(self,id):
        retorno = None
        for elem in self.listPCBs:
            if elem["id"] == id:
                retorno = elem["registroBase"]
        return retorno

    def getPCB(self,pid):
        for elem in self.listPCBs:
            if elem["id"] == pid:
                baseRegister = elem["registroBase"]
                limitRegister = elem["registroLimite"]
                ret = PCB(pid,baseRegister,limitRegister)
                break
        return ret

    def getRegistroLimiteDe(self,id):
        retorno = None
        for elem in self.listPCBs:
            if elem["id"] == id:
                retorno = elem["registroLimite"]
        return retorno

    def removePCBFromPage(self,pid):
        newList = []
        for elem in self.listPCBs:
            if elem["id"] != pid:
                newList.append(elem)
        self.listPCBs = newList

    def updateTable(self,memory):
        usedMemory = memory.getUsedMemory()
        for usedBlock in usedMemory:
            for elem in self.listPCBs:
                if usedBlock.getPID() == elem["id"]:
                    elem["registroBase"] = usedBlock.getBaseRegister()
                    elem["registroLimite"] = usedBlock.getLimitRegister()




