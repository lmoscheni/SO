'''
Created on 24/06/2013

@author: Leandro Moscheni
'''

class User():
    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.userType = GuestUser()
    
    def getName(self):
        return self.name
    
    def getPassword(self):
        return self.password
    
    def setPassword(self, password):
        self.password = password

    def isAdmind(self):
        return self.userType.isAdmin()

    def setAsAdmind(self):
        self.userType = AdministratorUser()

class GuestUser(User):
        
    def isAdmin(self):
        return False
    
class AdministratorUser(User):

    def isAdmin(self):
        return True