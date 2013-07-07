'''
Created on Jul 7, 2013

@author: Leandro Moscheni ; Julian Skalic
'''

class SchedulerPolicy():
    '''
       Entidad encargada de implementar las diferentes
       Politicas de Planificacion a corto plazo
    '''
        
class FIFO(SchedulerPolicy):
    '''
        Politica de planificacion FIFO:
        dada una cola de procesos p, donde p = [p1,p2,...,pn]
        Este algoritmo de planificacion, tomara el primer proceso
        que ingreso a la cola, sin ninguna otra evaluacion.
    '''
    
    def getProcess(self,queue):
        return queue.first()
    
class RoundRobin(SchedulerPolicy):
    '''
        Politica de planificacion RR:
        Esta politica actua, dandole a cada proceso una cantidad
        de ciclos determinado, luego de completar la cantidad de
        ciclos asignada, el proceso pasa al final de la cola 
        nuevamente, a esperar su turno.
        Por lo que para implementar el funcionamiento de este 
        algoritmo lo que haremos, es que antes luego de retornar
        el proceso, lo pondremos al final de la cola
    '''
    
    def getProcess(self,queue):
        process = queue.first()
        queue.dequeue()
        queue.add(process)
        
class Priority(SchedulerPolicy):
    '''
        Politica de planificacion Por Prioridad:
        Esta politica actua, dada una cola de procesos p, retorna
        al que mayor prioridad tenga.
        Para implementarla recorreremos la cola, e iremos preguntando
        prioridades, hasta terminar, y retornar al elemento de mayor
        prioridad
    '''
    
    def getProcess(self,queue):
        process = queue.first()
        for p in queue:
            if (p.priority() < process.priority()):
                process = p
        return process

        