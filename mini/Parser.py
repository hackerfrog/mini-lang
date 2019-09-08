from mini.Constants import *
from mini.Errors import *
from mini.Nodes import *
from mini.Result import *

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
        result = self.shift_expr()
        if not result.error and self.current_token.type != TT_EOF:
            return result.failure(InvalidSyntaxError(
                self.current_token.position_start, self.current_token.position_end,
                "Expected '+', '-', '*' or '/'"
            ))
        return result

    ## GRAMMER RULES ###########################################################

    def atom(self):
        result = ParserResult()
        token = self.current_token

        if token.type in (TT_INT, TT_FLOAT):
            result.register(self.advance())
            return result.success(NumberNode(token))
        elif token.type == TT_L_PAREN:
            result.register(self.advance())
            expr = result.register(self.expr())
            if result.error:
                return result
            if self.current_token.type == TT_R_PAREN:
                result.register(self.advance())
                return result.success(expr)
            else:
                return result.failure(InvalidSyntaxError(
                    self.current_token.position_start, self.current_token.position_end,
                    "Expected ')'"
                ))

        return result.failure(InvalidSyntaxError(
            token.position_start, token.position_end,
            "Expected type<int>, type<float>, +, - or ("
        ))

    def power(self):
        return self.binary_operation(self.atom, (TT_POWER, ), self.factor)

    def factor(self):
        result = ParserResult()
        token = self.current_token

        if token.type in (TT_PLUS, TT_MINUS):
            result.register(self.advance())
            factor = result.register(self.factor())
            if result.error:
                return result
            return result.success(UnaryOperationNode(token, factor))

        return self.power()

    def term(self):
        return self.binary_operation(self.factor, (TT_MULTIPLY, TT_DIVIDE, TT_MOD))

    def expr(self):
        return self.binary_operation(self.term, (TT_PLUS, TT_MINUS))
    
    def shift_expr(self):
        return self.binary_operation(self.expr, (TT_LSHIFT, TT_RSHIFT))

    def binary_operation(self, a_functionA, a_operations, a_functionB = None):
        if a_functionB == None:
            a_functionB = a_functionA

        result = ParserResult()
        left = result.register(a_functionA())
        if result.error:
            return result

        while self.current_token.type in a_operations:
            operator = self.current_token
            result.register(self.advance())
            right = result.register(a_functionB())
            if result.error:
                return result
            left = BinaryOperationNode(left, operator, right)

        return result.success(left)