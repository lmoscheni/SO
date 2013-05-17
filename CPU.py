class CPU():
    def __init__(self,tim,ck):
        self.timmer = tim
        self.clock = ck
        self.reg0 = 0
        self.reg1 = 0
        self.reg2 = 0
        self.reg3 = 0
        self.reg4 = 0
        self.reg5 = 0
        self.reg6 = 0
        self.reg7 = 0
        self.Z = False
        self.C = False
        self.O = False

    def initializeCPU(self):
        while True:
            self.clock.run()
            self.runInstruction()
            self.timmer.addCiclo()
            if self.timmer.renovacion == self.timmer.ciclos:
                self.timmer.reset()
                self.contextSwitch()

    def runInstruction(self):
        print("ejecutando instruccion")

    def contextSwitch(self):
        print("Haciendo cambio de contexto")
