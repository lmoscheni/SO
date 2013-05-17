# Importing User Hierarchy
import Users
# Importing Shell Exceptions
from ExceptionsShell import*

""" 
	author: Julian Skalick ; Leandro Moscheni.
	date: ...
	title: Shell
"""

# Class representing a shell, from the conceptual point of view of its 
# operation, so not interface and communication with the user.
class Shell():

    def __init__(self,usr,psw):
        self.users = []
        user = Users.UserAdmin(usr,psw)
        self.users.append(user)
        self.current = user
        print("The user: " + usr + " has been created")

# Shell Protocol Class

    """
    Method to create Users
    Precondition: The user creates a new user must be an administrator 
    and new user name should not be used by any other user already 
    belongs to Shell.
    """
    def createUser(self,usr,psw):
        if self.current.isAdmin():
            u = Users.UserGuest(usr,psw)
            self.users.append(u)
            print("The user: " + usr + " has been created")
        else:
            raise ExceptionNotIsAdmin("Only administrators can create users")

    """
    Method for logging a user in the Shell
    Precondition: The user must have been created previously.
    """
    def login(self,usr,pwd):
        for user in self.users:
            if usr == user.getName() and pwd == user.getPassword():
                self.current = user
                print("The user: " + usr + " has been created")
            else:
                raise ExceptionUserDontExist("The user entered does not exist or the password entered is not valid")

    """
    Method that allows a user to return as manager.
    Precondition: The user executing the order must be Administrator 
    and the user you want to return must be already created administrator.
    """
    def setAsAdmin(self,usr):
        if self.current.isAdmin():
            for user in self.users:
                if user.name == usr:
                    newUser = Users.UserAdmin(user.name,user.password)
                    self.users.remove(user)
                    self.users.append(newUser)
                    print("Now the user " + usr + "is Administrator.")
        else:
            raise ExceptionNotIsAdmin("Only Administrators can return to other users Administrators.")

    # Method that returns the name of the user logged
    def whoIm(self):
        print(self.current.getName())

    # Method for changing the logged in user's pasword.
    def changePasword(self,oldPassword,newPassword):
        if self.current.getPassword() == oldPassword:
            self.current.setPassword(newPassword)
        else:
            raise ExceptionErrorInOldPasword("The password entered is incorrect.")
