from Lexer import *

################################################################################
## RUN
################################################################################

def run(a_file_name, a_command):
    lexer = Lexer(a_file_name, a_command)
    tokens, error = lexer.make_tokens()

    return tokens, error