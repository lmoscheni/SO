import time
from Timmer import*

""" 
	author: Julian Skalick ; Leandro Moscheni.
	date: ...
	title: Clock
"""

"""
    Class that has the purpose of modeling the physical device 
    which generates the clock signal, so that the cpu works.
"""
class Clock():
    def __init__(self, win):
        self.window = win

    def run(self):
        return self.sleep()

    def sleep(self):
        time.sleep(self.window)


            
