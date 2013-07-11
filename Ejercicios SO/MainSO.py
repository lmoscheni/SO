from Programs import *
from HardDisk import *
from Kernel import *
from CPU import *
from InterruptionHandler import *
from PageTable import *

class Main():

    def run(self):
        instruccion = 1
        instruccion2 = 2
        instruccion3 = 3
        programa1 = Program("Programa1","")
        programa1.adInstruction(instruccion)
        programa1.adInstruction(instruccion)
        programa1.adInstruction(instruccion)
        programa2 = Program("Programa2","")
        programa2.adInstruction(instruccion2)
        programa2.adInstruction(instruccion2)
        programa2.adInstruction(instruccion2)
        programa3 = Program("Programa3","")
        programa3.adInstruction(instruccion3)
        programa3.adInstruction(instruccion3)
        programa3.adInstruction(instruccion3)
        programa3.adInstruction(instruccion3)


        hardDisk = HardDisk()
        hardDisk.save(programa1)
        hardDisk.save(programa2)
        hardDisk.save(programa3)
        #aImprimir = hardDisk.search("Programa2").getInstructions()[0]
        #print aImprimir

        pageTable = PageTable()
        memoria = Memoria(5,pageTable)

        intrHandler = InterruptionHandler(hardDisk,memoria,pageTable)

        cpu = CPU(2,intrHandler)

        kernel = Kernel(intrHandler)

        intrHandler.setCPU(cpu)
        intrHandler.setKernel(kernel)

        kernel.createProcess("Programa1")
        kernel.createProcess("Programa2")
        time.sleep(5)
        kernel.createProcess("Programa3")

SO = Main()
SO.run()
