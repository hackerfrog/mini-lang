################################################################################
## SYMBOL TABLE
################################################################################

class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.parent = None

    def get(self, a_variable):
        value = self.symbols.get(a_variable, None)
        if value == None and self.parent:
            return self.parent.get(a_variable)
        return value

    def set(self, a_variable, a_value):
        self.symbols[a_variable] = a_value

    def remove(self, a_variable):
        del self.symbols[a_variable]