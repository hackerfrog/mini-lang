################################################################################
## TOKENS
################################################################################

TT_INT              = 'INT'
TT_FLOAT            = 'FLOAT'
TT_PLUS             = 'PLUS'
TT_MINUS            = 'MINUS'
TT_MULTIPLY         = 'MUL'
TT_DIVIDE           = 'DIV'
TT_L_PAREN          = 'LPAREN'
TT_R_PAREN          = 'RPAREN'

class Token:
    def __init__(self, a_type, a_value=None):
        self.type = a_type
        self.value = a_value
    
    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'