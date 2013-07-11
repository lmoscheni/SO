'''
Created on 24/06/2013

@author: usuario
'''

class User():
    def __init__(self,name,password):
        self.name = name
        self.password = password
    
    def getName(self):
        return self.name
    
    def getPassword(self):
        return self.password
    
    def setPassword(self, password):
        self.password = password

class GuestUser(User):
    
    def __init__(self,name,password):
        User.__init__(self, name, password)
        
    def isAdmin(self):
        return False
    
class AdministratorUser(User):
    
    def __init__(self, name, password):
        User.__init__(self, name, password)

    def isAdmin(self):
        return True