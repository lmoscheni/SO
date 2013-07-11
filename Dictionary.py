'''
Created on Jul 7, 2013

@author: leandro
'''

class Dictionary():
    '''
        Representacion de una Estructura de Diccionario, sobre la que
        se pueden realizar busquedas, o agregar elemento que:
        key -> value
    '''
    def __init__(self):
        self.map = []

    def lookUp(self,key):
        retorno = None
        for e in self.map:
            if e.isSameKey(key):
                retorno = e.getValue()
                break
        if retorno == None:
            print "salta excepcion"
        return retorno

    def addToDictionary(self,key,value):
        element = Pair(key,value)
        self.map.append(element)

    def remove(self,key):
        self.map.remove(self.lookUp(key))


class Pair():
    '''
        Representacion de un par conformado por (key,value)
    '''
    def __init__(self,key,value):
        self.key = key
        self.value = value

    def getKey(self):
        return self.key

    def getValue(self):
        return self.value

    def isSameKey(self,key):
        return (self.key == key)
