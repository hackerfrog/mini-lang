################################################################################
## TOKENS
################################################################################

class Token:
    def __init__(self, a_type, a_value=None):
        self.type = a_type
        self.value = a_value
    
    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'