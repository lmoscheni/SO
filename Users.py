""" 
	author: Julian Skalick ; Leandro Moscheni.
	date: ...
	title: The User Hierarchy
"""

# Abstract class that generates a general structure of the users, 
# as well as a common protocol to them.
class User():

    def __init__(self,usr,pwd):
        self.name = usr
        self.password = pwd

# Setters and Getters
    def setPassword(self, pwd):
        self.password = pwd

    def getName(self):
        return self.name

    def getPassword(self):
        return self.pasword

    def isAdmin(self):
        return False

# Class that represents guests, whose permissions in principle limited.
class UserGuest(User):

    def __init__(self,usr,pwd):
        self.name = usr
        self.password = pwd

# Class representing Users Administrator, whose permissions in principle, 
# total.These users have permission to create or delete other users' and 
# return to a guest user, Administrator.
class UserAdmin(User):

    def __init__(self,usr,pwd):
        self.name = usr
        self.password = pwd

    def isAdmin(self):
        return True

