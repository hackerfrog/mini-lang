from mini.Lexer import *
from mini.Parser import *
from mini.Interpreter import *
from mini.Context import *
from mini.SymbolTable import *
from mini.Values import *

################################################################################
## RUN
################################################################################

global_symbol_table = SymbolTable()
global_symbol_table.set("NULL", Number(0))
global_symbol_table.set("TRUE", Number(1))
global_symbol_table.set("FALSE", Number(0))

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
    context = Context('<program>')
    context.symbol_table = global_symbol_table
    result = interpreter.visit(context, ast.node)

    return result.result, result.error