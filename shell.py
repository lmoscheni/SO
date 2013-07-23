'''
Created on 24/06/2013

@author: Leandro Moscheni ; Julin Skalic
'''

from user import *

# Representacion de un Shell
class Shell():
    def __init__(self, password,intrHandler):
        self.users = []
        self.programs ={"loggin" : self.loggin,
                        "whoIam" : self.whoIam,
                        "addUser" : self.addUser,
                        "changePassword" : self.changePassword,
                        "setAsAdmin" : self.setAsAdmin,
                        "ps" : self.ps,
                        "thatProcessIsRunning" : self.thatProcessIsRunning,
                        "FIFOImplement" : self.FIFOImplement,
                        "RRImplement" : self.RRImplement,
                        "PriorityImplement" : self.PriorityImplement,
                        "exit" : self.exit
                        }
        self.interruptionHandler = intrHandler
        self.interruptionHandler.setShell(self)
        self.users.append(AdministratorUser("Root",password))
        self.currentUser = None
        self.isRun = True
        self.initializePrompt()
    
    def initializePrompt(self):
        presentation = open("./presentacion",'r')
        print(presentation.read())
        presentation.close()
        statePrompt = " ~> "
        self.loggin()
        while self.isRun:
            input = raw_input(self.currentUser.getName() + statePrompt)
            try:
                p = self.programs[input]
                p()
            except:
                self.runCommand(input)

    # Nos permite iniciar sesion en el shell.
    def loggin(self):
        name = raw_input("Enter user name \n")
        password = raw_input("Enter a user password \n")
        self.currentUser = self.userIsValid(name,password)

    # Retorna el usuario asociado a (user,password) en caso de que exista,caso contrario
    # se lanza una excepcion
    def userIsValid(self,user,password):
        for u in self.users:
            if (u.getName() == user and u.getPassword() == password):
                return u
        raise Exception("El usuario no existe")

    # Permite saber quien es el usuario logueado
    def whoIam(self):
        print self.currentUser.getName()

    # Permite aniadir un usuario a la lista de usuarios del shell
    def addUser(self):
        name = raw_input("Enter new user name \n")
        password = raw_input("Enter a password for new user \n")
        if(self.currentUser.isAdmin()): self.users.append(GuestUser(name,password))

    # Permite cambiar el password actual, al usuario logueado,en caso de ingresar de
    # forma incorrecta el password actual se lanzara una excepcion indicando el error
    def changePassword(self):
        oldPass = raw_input("Enter actuall password")
        newPass = raw_input("Enter a new password")
        for u in self.users:
            if(u == self.currentUser and u.getPassword() == oldPass):
                u.setPassword(newPass)
            else:
                raise Exception("Password invalido")
    
    # Permite a un usuario administrador, volver usuario administrador a otro usuario
    # que no lo sea
    def setAsAdmin(self,nameUser):
        for u in self.users:
            if (u.getName() == nameUser):
                new = AdministratorUser(u.getName(),u.getPassword())
                self.users.remove(u)
                self.users.append(new)
    
    # Permite ejecutar un programa alojado en disco            
    def runCommand(self,anCommand):
        self.interruptionHandler.askTheKernelToCreateProcess(anCommand)

    # Permite mostrar texto en la consola, basicamente para notificacione de errores, etc
    def showMessageInTheDisplay(self,msj):
        self.notification = msj
     
    # Lista en pantalla los procesos que estan en la cola de readt   
    def ps(self):
        print "PID","  State"
        for p in self.interruptionHandler.kernel.readyQueue.queue:
            print p.getPID(),"   " + p.getState()
      
    # Retorna el proceso que actualmente esta corriendo la cpu      
    def thatProcessIsRunning(self):
        print self.interruptionHandler.returnCurrentProcess()
    
    # Estableze el algoritmo FIFO en la cola de ready    
    def FIFOImplement(self):
        self.interruptionHandler.FIFOQueue()
        
    # Establece el algoritmo RR en la cola de ready
    def RRImplement(self):
        q = raw_input("Enter a Quantum \n")
        self.interruptionHandler.RRQueue(q)
    
    # Establece el algoritmo por prioridad en la cola de readt
    def PriorityImplement(self):
        self.interruptionHandler.PriorityQueue()
        
    def exit(self):
        logs = open("./logsDeEjecucion",'w')
        logs.write("")
        logs.close()
        self.isRun = False