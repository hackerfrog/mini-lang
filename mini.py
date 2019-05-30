from Lexer import *
from Parser import *

################################################################################
## RUN
################################################################################

def run(a_file_name, a_command):
    lexer = Lexer(a_file_name, a_command)
    tokens, error = lexer.make_tokens()

    if error:
        return None, error

    ## Generate Abstract-Syntax-Tree ###########################################

    parser = Parser(tokens)
    ast = parser.parse()

    return ast, None