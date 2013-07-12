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
        self.queue.append(element)
        self.index = self.index + 1

    def remove(self,element):
        self.queue.remove(element)
    
    def dequeue(self):
        self.remove(self.first())

    def first(self):
        return self.queue[0]

    def isEmpty(self):
        return (self.queue == [])