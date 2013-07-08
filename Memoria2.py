from Bloque import *

class Memoria():
    def __init__(self):
        self.memoriaLibre = [Bloque(0,2024,None)]
        self.memoriaUsada = []
        self.estrategiaDeCarga = PeorAjuste()

    def setEstrategiaPrimerAjuste(self):
        self.estrategiaDeCarga = PrimerAjuste()

    def setEstrategiaMejorAjuste(self):
        self.estrategiaDeCarga = MejorAjuste()

    def setEstrategiaPeorAjuste(self):
        self.estrategiaDeCarga = PeorAjuste()

    def setMemoriaLibre(self,memoria):
        self.memoriaLibre = memoria

    def setMemoriaUsada(self,memoria):
        self.memoriaUsada = memoria

    def cargarEnMemoria(self,instrucciones):
        self.estrategiaDeCarga.cargar(self,instrucciones)

    def memoriaLibre(self):
        return self.memoriaLibre

    def agregarBloqueUsado(self,bloque):
        self.memoriaUsada.append(bloque)

    def agregarBloqueLibre(self,bloque):
        self.memoriaLibre.append(bloque)

    def leerMemoria(self,pos):
        instruccionARetornar = None
        posicion = pos-1
        for huecoUsado in self.memoriaUsada:
            if huecoUsado.posicionEstaDentroDeHueco(posicion):
                instruccionARetornar = huecoUsado.leerInstruccion(posicion)
                self.comprobarTerminacion(huecoUsado,posicion)
                break
        return instruccionARetornar

    def comprobarTerminacion(self,bloque,pos):
        for huecoUsado in self.memoriaUsada:
            if (huecoUsado == bloque) & (huecoUsado.getRegistroLimite() == pos):
                self.removerBloqueUsado(huecoUsado)
                nuevoBloqueLibre = Bloque(huecoUsado.getRegistroBase(),huecoUsado.getRegistroLimite(),None)
                self.agregarBloqueLibre(nuevoBloqueLibre)
                break

    def existeBloqueDisponible(self,instrucciones):
        retorno = False
        for huecoLibre in self.memoriaLibre:
            if huecoLibre.espacioEnBloque()+1 >= len(instrucciones):
                retorno = True
                break
        return retorno

    def existeMemoriaDisponible(self,instrucciones):
        retorno = False
        memoria = 0
        for huecoLibre in self.memoriaLibre:
            memoria = memoria + huecoLibre.espacioEnBloque() + 1
        if memoria >= len(instrucciones):
            retorno = True
        return retorno

    def fragmentarMemoria(self):
        self.fragmentarBloquesUsados()
        self.fragmentarBloquesLibres()

    def fragmentarBloquesLibres(self):
        memoria = 0
        registroLimiteDeUltimoBloqueOcupado = (self.memoriaUsada[len(self.memoriaUsada)-1]).getRegistroLimite()
        for huecoLibre in self.memoriaLibre:
            memoria = memoria + huecoLibre.espacioEnBloque()
        self.memoriaLibre = []
        registroBase = registroLimiteDeUltimoBloqueOcupado+1
        registroLimite = registroBase+memoria+1
        self.memoriaLibre.append(Bloque(registroBase,registroLimite,None))

    def fragmentarBloquesUsados(self):
        numeroBloque = 0
        bloqueAnterior = None
        for huecoUsado in self.memoriaUsada:
            if numeroBloque == 0:
                espacioEnBloqueUsado = huecoUsado.espacioEnBloque()
                huecoUsado.setRegistroBase(0)
                huecoUsado.setRegistroLimite(espacioEnBloqueUsado)
            else:
                huecoUsado.setRegistroBase(bloqueAnterior.getRegistroLimite() + 1)
                huecoUsado.setRegistroLimite(huecoUsado.getRegistroBase() + huecoUsado.espacioEnBloque())
            bloqueAnterior = huecoUsado
            numeroBloque = numeroBloque + 1

    def removerBloqueUsado(self,bloque):
        listaNueva = []
        for huecoUsado in self.memoriaUsada:
            if huecoUsado != bloque:
                listaNueva.append(huecoUsado)
        self.setMemoriaUsada(listaNueva)

    def mostrar(self):
        for huecoLibre in self.memoriaLibre:
            print huecoLibre.getRegistroBase()
            print huecoLibre.getRegistroLimite()
        print "\n"
        for huecoUsado in self.memoriaUsada:
            print huecoUsado.getRegistroBase()
            print huecoUsado.getRegistroLimite()


class EstrategiaDeCarga():
    def cargar(self,mem,instrucciones):
        print

    def removerBloque(self,mem,bloque):
        listaNueva = []
        for huecoLibre in mem.memoriaLibre:
            if huecoLibre != bloque:
                listaNueva.append(huecoLibre)
        mem.setMemoriaLibre(listaNueva)


class PrimerAjuste(EstrategiaDeCarga):

    def cargar(self,mem,instrucciones):
        if mem.existeBloqueDisponible(instrucciones):
            self.cargarEnBloque(mem,instrucciones)
        else:
            if mem.existeMemoriaDisponible(instrucciones):
                mem.fragmentarMemoria()
                self.cargarEnBloque(mem,instrucciones)
            else:
                print "No hay memoria"

    def cargarEnBloque(self,mem,instrucciones):
        for huecoLibre in mem.memoriaLibre:
            if huecoLibre.espacioEnBloque()+1 >= len(instrucciones):
                registroInstrucciones = len(instrucciones)
                nuevoBloqueUsado = Bloque(huecoLibre.getRegistroBase(),huecoLibre.getRegistroBase() + registroInstrucciones-1,instrucciones)
                mem.agregarBloqueUsado(nuevoBloqueUsado)
                registroBase = huecoLibre.getRegistroBase()
                registroLimite = huecoLibre.getRegistroLimite()
                if registroBase+registroInstrucciones <= registroLimite:
                    huecoLibre.setRegistroBase(huecoLibre.getRegistroBase()+registroInstrucciones)
                else:
                    self.removerBloque(mem,huecoLibre)
                break



class MejorAjuste(EstrategiaDeCarga):

    def cargar(self,mem,instrucciones):
        if mem.existeBloqueDisponible(instrucciones):
            self.cargarEnBloque(mem,instrucciones)
        else:
            if mem.existeMemoriaDisponible(instrucciones):
                mem.fragmentarMemoria()
                self.cargarEnBloque(mem,instrucciones)
            else:
                print "No hay memoria"

    def cargarEnBloque(self,mem,instrucciones):
        bloqueACargar = self.buscarBloqueQueSeAjusteA(mem,instrucciones)
        registroInstrucciones = len(instrucciones)
        nuevoBloqueUsado = Bloque(mem.memoriaLibre[bloqueACargar].getRegistroBase(),mem.memoriaLibre[bloqueACargar].getRegistroBase() + registroInstrucciones-1,instrucciones)
        mem.agregarBloqueUsado(nuevoBloqueUsado)
        registroBase = mem.memoriaLibre[bloqueACargar].getRegistroBase()
        registroLimite = mem.memoriaLibre[bloqueACargar].getRegistroLimite()
        if registroBase+registroInstrucciones <= registroLimite:
            mem.memoriaLibre[bloqueACargar].setRegistroBase(mem.memoriaLibre[bloqueACargar].getRegistroBase()+registroInstrucciones)
        else:
            self.removerBloque(mem,mem.memoriaLibre[bloqueACargar])

    def primerDiferenciaPositiva(self,mem,instrucciones):
        retorno = None
        for huecoLibre in mem.memoriaLibre:
            if ((huecoLibre.espacioEnBloque()+1) - len(instrucciones)) >=0:
                retorno =huecoLibre.espacioEnBloque()+1 - len(instrucciones)
                break
        return retorno

    def buscarBloqueQueSeAjusteA(self,mem,instrucciones):
        diferencia = self.primerDiferenciaPositiva(mem,instrucciones)
        bloque = 0
        retorno = 0
        for huecoLibre in mem.memoriaLibre:
            diferenciaActual = huecoLibre.espacioEnBloque()+1 - len(instrucciones)
            if (diferenciaActual >= 0) & (diferencia >= diferenciaActual):
                diferencia = diferenciaActual
                retorno = bloque
            bloque = bloque + 1
        return retorno


class PeorAjuste(EstrategiaDeCarga):

    def cargar(self,mem,instrucciones):
        if mem.existeBloqueDisponible(instrucciones):
            self.cargarEnBloque(mem,instrucciones)
        else:
            if mem.existeMemoriaDisponible(instrucciones):
                mem.fragmentarMemoria()
                self.cargarEnBloque(mem,instrucciones)
            else:
                print "No hay memoria"

    def buscarBloqueMasGrande(self,mem,instrucciones):
        bloque = 0
        retorno = 0
        huecoMasGrande = 0
        for huecoLibre in mem.memoriaLibre:
            if huecoLibre.espacioEnBloque()+1 > huecoMasGrande:
                huecoMasGrande = huecoLibre.espacioEnBloque()+1
                retorno = bloque
            bloque = bloque + 1
        return retorno

    def cargarEnBloque(self,mem,instrucciones):
        bloqueACargar = self.buscarBloqueMasGrande(mem,instrucciones)
        registroInstrucciones = len(instrucciones)
        nuevoBloqueUsado = Bloque(mem.memoriaLibre[bloqueACargar].getRegistroBase(),mem.memoriaLibre[bloqueACargar].getRegistroBase() + registroInstrucciones-1,instrucciones)
        mem.agregarBloqueUsado(nuevoBloqueUsado)
        registroBase = mem.memoriaLibre[bloqueACargar].getRegistroBase()
        registroLimite = mem.memoriaLibre[bloqueACargar].getRegistroLimite()
        if registroBase+registroInstrucciones <= registroLimite:
            mem.memoriaLibre[bloqueACargar].setRegistroBase(mem.memoriaLibre[bloqueACargar].getRegistroBase()+registroInstrucciones)
        else:
            self.removerBloque(mem,mem.memoriaLibre[bloqueACargar])



