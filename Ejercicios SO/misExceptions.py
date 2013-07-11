class ExceptionInvalidUser(Exception):
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return repr(self.valor)

class ExceptionInvalidPassword(Exception):
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return repr(self.valor)

class ExceptionNotAdministrator(Exception):
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return repr(self.valor)

class ExceptionNoProgramInDisk(Exception):
    def __init__(self,valor):
        self.valor = valor
    def __str__(self):
        return repr(self.valor)

class ExceptionNoMemory(Exception):
    def __init__(self,valor):
        self.valor = valor
    def __str__(self):
        return repr(self.valor)
