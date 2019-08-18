from mini.Constants import *
from mini.Errors import *
from mini.Nodes import *
from mini.ParserResult import *

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
        if not result.error and self.current_token.type != TT_EOF:
            return result.failure(InvalidSyntaxError(
                self.current_token.position_start, self.current_token.position_end,
                "Expected '+', '-', '*' or '/'"
            ))
        return result

    ## GRAMMER RULES ###########################################################

    def factor(self):
        result = ParserResult()
        token = self.current_token

        if token.type in (TT_INT, TT_FLOAT):
            result.register(self.advance())
            return result.success(NumberNode(token))

        return result.failure(InvalidSyntaxError(
            token.position_start, token.position_end,
            "Expected type<int> or type<float>"
        ))

    def term(self):
        return self.binary_operation(self.factor, (TT_MULTIPLY, TT_DIVIDE))

    def expr(self):
        return self.binary_operation(self.term, (TT_PLUS, TT_MINUS))

    def binary_operation(self, a_function, a_operations):
        result = ParserResult()
        left = result.register(a_function())
        if result.error:
            return result

        while self.current_token.type in a_operations:
            operator = self.current_token
            result.register(self.advance())
            right = result.register(a_function())
            if result.error:
                return result
            left = BinaryOperationNode(left, operator, right)

        return result.success(left)