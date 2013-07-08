'''
Created on Jul 7, 2013

@author: Leandro Moscheni ; Julian Skalic
'''

class Queue():
    '''
        Representacion de la Estructura de Cola
    '''
    def __init__(self):
        self.index = 0
        self.queue = []
        
    def add(self,element):
        self.queue.insert(self.index, element)
        self.index = self.index + 1
        
    def remove(self,element):
        self.queue.remove(element)
        
    def first(self):
        return self.queue[0]
        
        