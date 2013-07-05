'''
Created on 24/06/2013

@author: Leandro Moscheni ; Julin Skalic
'''

from user import *

"""
    Funciones empleadas para la lectura de la entrada del shell
"""
# Dado un String, retorna la longitud del mismo
def size(cadena):
    ret = 0
    for i in cadena:
        ret = ret + 1
    return ret

# Funcion que permite la separacion en tokens de la entrada por teclado
def generateTokens(ent):
        y = ""
        lista = []
        val = size(ent)
        for x in (ent + " "):
            if((x != ' ') & (val != 0)):
                y = y + x
            else:
                lista.append(y)
                y = ""
            val = val-1
        return lista

# Representacion de un Shell
class Shell():
    def __init__(self, password):
        self.users = []
        self.users.append(AdministratorUser("Root",password))
        self.currentUser = None
        self.initializePrompt()
    
    def initializePrompt(self):
        statePrompt = "~> "
        print "Hello"
        print "Now log in with a user"
        print "Enter the user name"
        name = raw_input()
        print "Enter the user password"
        password = raw_input()
        self.loggin(name,password)
        while True:
            print self.currentUser.getName() , statePrompt
            input = raw_input()
            if(input == "exit"): break
            tokens = generateTokens(input)
            if(tokens[0] == "loggin"): self.loggin(tokens[1], tokens[2])
            if(tokens[0] == "changePassword"): self.changePassword(tokens[1], tokens[2])
            if(tokens[0] == "addUser"): self.addUser(tokens[1], tokens[2])
            if(tokens[0] == "whoIm"): self.whoIm()
            if(tokens[0] == "setAsAdmin") : self.setAsAdmin(tokens[1])
            #Hay que hacer que interactue con el Kernel, para buscar el programa en Disco
    
    # Nos permite iniciar sesion en el shell.
    def loggin(self,user,password):
            self.currentUser = self.userIsValid(user,password)

    # Retorna el usuario asociado a (user,password) en caso de que exista,caso contrario
    # se lanza una excepcion
    def userIsValid(self,user,password):
        for u in self.users:
            if (u.getName() == user and u.getPassword() == password):
                return u
        print "El usuario no existe"
    
    # Permite saber quien es el usuario logueado
    def whoIm(self):
        print self.currentUser.getName()
    
    # Permite añadir un usuario a la lista de usuarios del shell
    def addUser(self,name,password):
        if(self.currentUser.isAdmin()): self.users.append(GuestUser(name,password))

    # Permite cambiar el password actual, al usuario logueado,en caso de ingresar de
    # forma incorrecta el password actual se lanzara una excepcion indicando el error
    def changePassword(self,oldPass, newPass):
        for u in self.users:
            if(u == self.currentUser and u.getPassword() == oldPass):
                u.setPassword(newPass)
            else:
                print "el Password es incorrecto"
    
    # Permite a un usuario administrador, volver usuario administrador a otro usuario
    # que no lo sea
    def setAsAdmin(self,nameUser):
        for u in self.users:
            if (u.getName() == nameUser):
                new = AdministratorUser(u.getName(),u.getPassword())
                this.users.remove(u)
                this.users.append(new)
