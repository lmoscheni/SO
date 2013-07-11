from Bloque import *
from Programs import *
from PCB import *
from misExceptions import *

class Memoria():
    def __init__(self,tamMemory):
        self.freeMemory = [Block(0,tamMemory,None)]
        self.usedMemory = []
        self.loadStrategy = FirstFit()

    #Setea la estrategia primer ajuste
    def setFirstFitStrategy(self):
        self.loadStrategy = FirstFit()

    #Setea la estrategia mejor ajuste
    def setBestFitStrategy(self):
        self.loadStrategy = BestFit()

    #Setea la estrategia peor ajuste
    def setWorstFitStrategy(self):
        self.loadStrategy = WorstFit()

    #Setea la lista de bloques libres
    def setFreeMemory(self,memory):
        self.freeMemory = memory

    #Setea la lista de bloques ocupados
    def setUsedMemory(self,memory):
        self.usedMemory = memory

    #Carga las instrucciones de un programa en memoria
    def load(self, program):
        instructions = program.getInstructions()
        return self.loadStrategy.load(self,instructions)

    #Retorna la memoria libre
    def getFreeMemory(self):
        return self.freeMemory

    #Agrega un bloque usado a la lista de bloques usados
    def addUsedBlock(self,block):
        self.usedMemory.append(block)

    #Agrega un bloque libre a la lista de bloques libres
    def addFreeBlock(self,block):
        self.freeMemory.append(block)

    #Lee una instruccion de memoria
    def read(self,pos):
        returnInstruction = None
        position = pos
        for usedBlock in self.usedMemory:
            if usedBlock.positionInsideBlock(position):
                returnInstruction = usedBlock.readInstruction(position)
                break
        if returnInstruction == None: raise ExceptionNoInstructionOnMemory("No existe la instruccion en memoria")
        else: return returnInstruction

    #Libera espacio en memoria
    def free(self,process):
        base = process.getInicio()
        for usedBlock in  self.usedMemory:
            if usedBlock.getBaseRegister() == base:
                self.removeUsedBlock(usedBlock)
                newFreeBlock = Block(usedBlock.getBaseRegister(),usedBlock.getLimitRegister(),None)
                self.addFreeBlock(newFreeBlock)

    #Verifica si existe un bloque disponible
    def existAvailableBlock(self,instructions):
        ret = False
        for freeBlock in self.freeMemory:
            if freeBlock.spaceOnBlock()+1 >= len(instructions):
                ret = True
                break
        return ret

    #Verifica si existe memoria disponible
    def existAvailableMemory(self,instructions):
        memory = 0
        for freeBlock in self.freeMemory:
            memory = memory + freeBlock.spaceOnBlock() + 1
        if memory >= len(instructions): return True
        else: return False

    #Fragmenta la memoria
    def fragmenMemory(self):
        self.fragmentUsedBlocks()
        self.fragmentFreeBlocks()

    #Fragmenta los bloques usados formando un solo bloque libre
    def fragmentFreeBlocks(self):
        memory = 0
        limitRegisterOfLastBlockUsed = (self.usedMemory[len(self.usedMemory)-1]).getLimitRegister()
        for freeBlock in self.freeMemory: memory = memory + freeBlock.spaceOnBlock()
        self.freeMemory = []
        baseRegister = limitRegisterOfLastBlockUsed + 1
        limitRegister = baseRegister + memory + 1
        self.freeMemory.append(Block(baseRegister,limitRegister,None))

    #Fragmenta los bloques usados, moviendolos al principio de la memoria
    def fragmentUsedBlocks(self):
        blockNumber = 0
        previousBlock = None
        for usedBlock in self.usedMemory:
            if blockNumber == 0:
                spaceInUsedBlock = usedBlock.spaceOnBlock()
                usedBlock.setBaseRegister(0)
                usedBlock.setLimitRegister(spaceInUsedBlock)
            else:
                usedBlock.setBaseRegister(previousBlock.getLimitRegister() + 1)
                usedBlock.setLimitRegister(usedBlock.getBaseRegister() + usedBlock.spaceOnBlock())
            previousBlock = usedBlock
            blockNumber+=1

    #Remueve el bloque usado
    def removeUsedBlock(self,block):
        newList = []
        for usedBlock in self.usedMemory:
            if usedBlock != block: newList.append(usedBlock)
        self.setUsedMemory(newList)

    def mostrar(self):
        for huecoLibre in self.memoriaLibre:
            print huecoLibre.getRegistroBase()
            print huecoLibre.getRegistroLimite()
        print "\n"
        for huecoUsado in self.memoriaUsada:
            print huecoUsado.getRegistroBase()
            print huecoUsado.getRegistroLimite()


class LoadStrategy():

    #Remueve un bloque libre de memoria
    def removeBlock(self,memory,block):
        newList = []
        for freeBlock in memory.getFreeMemory():
            if freeBlock != block: newList.append(freeBlock)
        memory.setFreeMemory(newList)


class FirstFit(LoadStrategy):

    #Verifica memoria disponible y carga instrucciones en el bloque correcto
    def load(self,memory,instructions):
        ret = None
        if memory.existAvailableBlock(instructions): ret = self.loadInBlock(memory,instructions)
        else:
            if memory.existAvailableMemory(instructions):
                memory.fragmentMemory()
                ret = self.loadInBlock(memory,instructions)
            else: raise ExceptionNoMemory("No hay memoria")
        return ret

    #Carga las instrucciones en el bloque
    def loadInBlock(self,memory,instructions):
        ret = None
        for freeBlock in memory.getFreeMemory():
            if freeBlock.spaceOnBlock()+1 >= len(instructions):
                registerInstruction = len(instructions)
                newUsedBlock = Block(freeBlock.getBaseRegister(),freeBlock.getBaseRegister() + registerInstruction-1,instructions)
                memory.addUsedBlock(newUsedBlock)
                baseRegister = freeBlock.getBaseRegister()
                limitRegister = freeBlock.getLimitRegister()
                ret = newUsedBlock
                if baseRegister+registerInstruction <= limitRegister: freeBlock.setBaseRegister(freeBlock.getBaseRegister()+registerInstruction)
                else: self.removeBlock(memory,freeBlock)
                break
        return ret


class BestFit(LoadStrategy):

    #Verifica memoria disponible y carga instrucciones en bloque correcto
    def load(self,memory,instructions):
        ret = None
        if memory.existAvailableBlock(instructions): ret = self.loadInBlock(memory,instructions)
        else:
            if memory.existAvailableMemory(instructions):
                memory.fragmentMemory()
                ret = self.loadInBlock(memory,instructions)
            else: raise ExceptionNoMemory("No hay memoria")
        return ret

    #Carga las instrucciones en el bloque
    def loadInBlock(self,memory,instructions):
        ret = None
        loadABlock = self.searchFitBlock(memory,instructions)
        registerInstruction = len(instructions)
        newUsedBlock = Block(memory.getFreeMemory()[loadABlock].getBaseRegister(),memory.getFreeMemory()[loadABlock].getBaseRegister() + registerInstruction-1,instructions)
        memory.addUsedBlock(newUsedBlock)
        baseRegister = memory.getFreeMemory()[loadABlock].getBaseRegister()
        limitRegister = memory.getFreeMemory[loadABlock].getLimitRegister()
        ret = newUsedBlock
        if (baseRegister + registerInstruction) <= limitRegister: memory.getFreeMemory()[loadABlock].setBaseRegister(memory.getFreeMemory[loadABlock].getBaseRegister()+registerInstruction)
        else: self.removeBlock(memory,memory.getFreeMemory()[loadABlock])
        return ret

    #Busca la primer diferencia positiva que hay entre el espacion en el bloque
    #y la cantidad de instrucciones a cargar
    def firstPositiveDiference(self,memory,instructions):
        ret = None
        for freeBlock in memory.getFreeMemory():
            if ((freeBlock.spaceOnBlock()+1) - len(instructions)) >=0:
                ret = freeBlock.spaceOnBlock()+1 - len(instructions)
                break
        return ret

    #Busca el bloque que mejor se ajusta a la cantidad de instrucciones a cargar
    def searchFitBlock(self,memory,instructions):
        diference = self.firstPositiveDiference(memory,instructions)
        block = 0
        ret = 0
        for freeBlock in memory.getFreeMemory():
            actualDiference = freeBlock.spaceOnBlock()+1 - len(instructions)
            if (actualDiference >= 0) & (diference >= actualDiference):
                diference = actualDiference
                ret = block
            block += 1
        return ret


class WorstFit(LoadStrategy):

    #Verifica memoria disponible y carga instrucciones en bloque correcto
    def load(self,memory,instructions):
        ret = None
        if memory.existAvailableBlock(instructions): ret = self.loadInBlock(memory,instructions)
        else:
            if memory.existAvailableMemory(instructions):
                memory.fragmentMemory()
                ret = self.loadInBlock(memory,instructions)
            else: raise ExceptionNoMemory("No hay memoria")
        return ret

    #Busca el bloque mas grande
    def searchBigrBlock(self,memory,instructions):
        block = 0
        ret = 0
        bigBlock = 0
        for freeBlock in memory.getFreeMemory():
            if freeBlock.spaceOnBlock()+1 > bigBlock:
                bigBlock = freeBlock.spaceOnBlock()+1
                ret = block
            block += 1
        return ret

    #Carga las instrucciones en el bloque
    def loadInBlock(self,memory,instructions):
        ret = None
        loadABlock = self.searchBigrBlock(memory,instructions)
        registerInstruction = len(instructions)
        newUsedBlock = Block(memory.getFreeMemory()[loadABlock].getBaseRegister(),memory.getFreeMemory()[loadABlock].getBaseRegister() + registerInstruction-1,instructions)
        memory.addUsedBlock(newUsedBlock)
        baseRegister = memory.getFreeMemory()[loadABlock].getBaseRegister()
        limitRegister = memory.getFreeMemory()[loadABlock].getLimitRegister()
        ret = newUsedBlock
        if (baseRegister + registerInstruction) <= limitRegister: memory.getFreeMemory()[loadABlock].setBaseRegister(memory.getFreeMemory()[loadABlock].getBaseRegister()+registerInstruction)
        else: self.removeBlock(memory,memory.getFreeMemory()[loadABlock])
        return ret


