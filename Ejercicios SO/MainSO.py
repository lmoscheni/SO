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
        programa1 = Program("Programa1","")
        programa1.adInstruction(instruccion)
        programa1.adInstruction(instruccion)
        programa1.adInstruction(instruccion)
        programa2 = Program("Programa2","")
        programa2.adInstruction(instruccion2)
        programa2.adInstruction(instruccion2)
        programa2.adInstruction(instruccion2)


        hardDisk = HardDisk()
        hardDisk.save(programa1)
        hardDisk.save(programa2)
        #aImprimir = hardDisk.search("Programa2").getInstructions()[0]
        #print aImprimir

        #pageTable = PageTable()
        memoria = Memoria(1024)

        intrHandler = InterruptionHandler(hardDisk,memoria)

        cpu = CPU(2,intrHandler)

        kernel = Kernel(intrHandler)

        intrHandler.setCPU(cpu)
        intrHandler.setKernel(kernel)

        kernel.createProcess("Programa1")
        #time.sleep(1)
        kernel.createProcess("Programa2")

SO = Main()
SO.run()
