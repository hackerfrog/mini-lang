from mini.Lexer import *
from mini.Parser import *
from mini.Interpreter import *

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

    if ast.error:
        return None, ast.error

    ## Run Program #############################################################
    interpreter = Interpreter()
    result = interpreter.visit(ast.node)

    return result.value, None