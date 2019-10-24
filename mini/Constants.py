import string

################################################################################
## CONSTANTS
################################################################################

DIGITS                  = '0123456789'
LETTERS                 = string.ascii_letters
LETTERS_DIGITS          = LETTERS + DIGITS

TT_INT                  = 'INT'
TT_FLOAT                = 'FLOAT'

TT_PLUS                 = 'PLUS'
TT_MINUS                = 'MINUS'
TT_MULTIPLY             = 'MUL'
TT_DIVIDE               = 'DIV'
TT_MOD                  = 'MOD'
TT_POWER                = 'POW'
TT_EQUAL                = 'EQUAL'

TT_L_PAREN              = 'LPAREN'
TT_R_PAREN              = 'RPAREN'

TT_LSHIFT               = 'LSHIFT'
TT_RSHIFT               = 'RSHIFT'

TT_BIT_NOT              = 'BIT-NOT'
TT_BIT_AND              = 'BIT-AND'
TT_BIT_XOR              = 'BIT-XOR'
TT_BIT_OR               = 'BIT-OR'

TT_DOUBLE_EQUAL         = 'EQUAL-TO'
TT_NOT_EQUAL            = 'NOT-EQUAL'
TT_LESS_THAN            = 'LESS-THAN'
TT_GREATER_THAN         = 'GREATER-THAN'
TT_LESS_THAN_EQUAL      = 'LESS-THAN-EQUAL'
TT_GREATER_THAN_EQUAL   = 'GREATER-THAN-EQUAL'

TT_EOF                  = 'EOF'

TT_IDENTIFIER           = 'IDENTIFIER'
TT_KEYWORD              = 'KEYWORD'

KEYWORDS                = [
    'VAR',
    'AND',
    'OR',
    'NOT',
    'IF',
    'THEN',
    'ELIF',
    'ELSE',
    'FOR',
    'TO',
    'STEP',
    'WHILE'
]