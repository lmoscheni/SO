"""
	authors: Julian Skalick ; Leandro Moscheni.
	date: ...
	title: Shell Exceptions
"""

# Error except for administrator authentication
class ExceptionNotIsAdmin(Exception):

    def __init__(self, val):
        self.value = val

    def __str__(self):
        return repr(self.value)

# Exception error by introducing the old password
class ExceptionErrorInOldPassword(Exception):

    def __init__(self, val):
        self.value = val

    def __str__(self):
        return repr(self.value)
# Exception error, lack of user logged
class ExceptionUserDontExist(Exception):
    def __init__(self,val):
        self.value = val

    def __str__(self):
        return repr(self.value)
