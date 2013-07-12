'''
Created on Jul 11, 2013

@author: leandro
'''
from Cola import *
from PCB import *

p1 = PCB(1,0,3)
p2 = PCB(2,4,5)
p3 = PCB(3,6,8)
p4 = PCB(4,9,10)

queue = Queue()

queue.add(p1)
queue.add(p2)
queue.add(p3)
queue.add(p4)

print "Ponemos el pid del primer proceso"
print queue.first().getPID()

print "Ponemos el pid de todos los procesos que hay en la cola"
queue.dequeue()

for i in queue.queue:
    print i.getPID()
    
