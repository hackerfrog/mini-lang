from mini.Constants import *
from mini.Nodes import *

################################################################################
## PARSER
################################################################################

class Parser:
    def __init__(self, a_tokens):
        self.tokens = a_tokens
        self.token_index = -1
        self.advance()

    def advance(self):
        self.token_index += 1
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
        
        return self.current_token

    def parse(self):
        result = self.expr()
        return result

    ## GRAMMER RULES ###########################################################

    def factor(self):
        token = self.current_token

        if token.type in (TT_INT, TT_FLOAT):
            self.advance()
            return NumberNode(token)

    def term(self):
        return self.binary_operation(self.factor, (TT_MULTIPLY, TT_DIVIDE))

    def expr(self):
        return self.binary_operation(self.term, (TT_PLUS, TT_MINUS))
    
    def binary_operation(self, a_function, a_operations):
        left = a_function()

        while self.current_token.type in a_operations:
            operator = self.current_token
            self.advance()
            right = a_function()
            left = BinaryOperationNode(left, operator, right)
        
        return left