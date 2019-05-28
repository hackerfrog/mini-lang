from Lexer import *

################################################################################
## RUN
################################################################################

def run(a_command):
    lexer = Lexer(a_command)
    tokens, error = lexer.make_tokens()

    return tokens, error