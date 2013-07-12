'''
Created on Jul 11, 2013

@author: leandro
'''
import types
from HardDisk import *
from Programs import *
from Instructions import *

class IOSystem():

    def __init__(self):
        self.devices = []
        
    def addDevice(self,d):
        self.devices.append(d)
        
    def getProgram(self,anProgram):
        for d in self.devices:
            if isinstance(d,HardDisk): return d.search(anProgram)
