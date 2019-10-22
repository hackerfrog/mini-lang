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
        result = self.assign()
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
            result.register_advancement()
            self.advance()
            return result.success(NumberNode(token))
        elif token.type == TT_IDENTIFIER:
            result.register_advancement()
            self.advance()
            return result.success(VariableAccessNode(token))
        elif token.type == TT_L_PAREN:
            result.register_advancement()
            self.advance()
            expr = result.register(self.expr())
            if result.error:
                return result
            if self.current_token.type == TT_R_PAREN:
                result.register_advancement()
                self.advance()
                return result.success(expr)
            else:
                return result.failure(InvalidSyntaxError(
                    self.current_token.position_start, self.current_token.position_end,
                    "Expected ')'"
                ))

        return result.failure(InvalidSyntaxError(
            token.position_start, token.position_end,
            "Expected type<int>, type<float>, IDENTIFIER, +, - or ("
        ))

    def power(self):
        return self.binary_operation(self.atom, (TT_POWER, ), self.factor)

    def bit_not(self):
        result = ParserResult()
        token = self.current_token

        if token.type in (TT_BIT_NOT,):
            result.register_advancement()
            self.advance()
            bit_not = result.register(self.bit_not())
            if result.error:
                return result
            return result.success(UnaryOperationNode(token, bit_not))

        return self.power()

    def factor(self):
        result = ParserResult()
        token = self.current_token

        if token.type in (TT_PLUS, TT_MINUS):
            result.register_advancement()
            self.advance()
            factor = result.register(self.factor())
            if result.error:
                return result
            return result.success(UnaryOperationNode(token, factor))

        return self.bit_not()

    def term(self):
        return self.binary_operation(self.factor, (TT_MULTIPLY, TT_DIVIDE, TT_MOD))

    def expr(self):
        return self.binary_operation(self.term, (TT_PLUS, TT_MINUS))

    def shift_expr(self):
        return self.binary_operation(self.expr, (TT_LSHIFT, TT_RSHIFT))

    def bit_and(self):
        return self.binary_operation(self.shift_expr, (TT_BIT_AND, ))

    def bit_xor(self):
        return self.binary_operation(self.bit_and, (TT_BIT_XOR, ))

    def bit_or(self):
        return self.binary_operation(self.bit_xor, (TT_BIT_OR, ))

    def comp_expr(self):
        result = ParserResult()
        if self.current_token.matches(TT_KEYWORD, 'NOT'):
            token = self.current_token
            result.register_advancement()
            self.advance()

            comp_expr = result.register(self.comp_expr())
            if result.error:
                return result
            return result.success(UnaryOperationNode(token, comp_expr))

        node = result.register(self.binary_operation(self.bit_or, (TT_DOUBLE_EQUAL, TT_NOT_EQUAL, TT_LESS_THAN, TT_GREATER_THAN, TT_LESS_THAN_EQUAL, TT_GREATER_THAN_EQUAL)))

        if result.error:
            return result.failure(InvalidSyntaxError(
                self.current_token.position_start, self.current_token.position_end,
                "Expected type<int>, type<float>, IDENTIFIER, +, -, ( or keyword<NOT>"
            ))

        return result.success(node)

    def bool_expr(self):
        return self.binary_operation(self.comp_expr, ((TT_KEYWORD, 'AND'), (TT_KEYWORD, 'OR')))

    def assign(self):
        result = ParserResult()
        if self.current_token.matches(TT_KEYWORD, 'VAR'):
            result.register_advancement()
            self.advance()

            if self.current_token.type != TT_IDENTIFIER:
                return result.failure(InvalidSyntaxError(
                    self.current_token.position_start, self.current_token.position_end,
                    'Expected IDENTIFIER'
                ))

            variable = self.current_token
            result.register_advancement()
            self.advance()

            if self.current_token.type != TT_EQUAL:
                return result.failure(InvalidSyntaxError(
                    self.current_token.position_start, self.current_token.position_end,
                    "Expected '='"
                ))

            result.register_advancement()
            self.advance()
            bool_expr = result.register(self.bool_expr())
            if result.error:
                return result
            return result.success(VariableAssignNode(variable, bool_expr))

        node = result.register(self.bool_expr())
        if result.error:
            return result.failure(InvalidSyntaxError(
                self.current_token.position_start, self.current_token.position_end,
                "Expected type<int>, type<float>, IDENTIFIER, VAR, +, - or ("
            ))
        return result.success(node)


    def binary_operation(self, a_functionA, a_operations, a_functionB = None):
        if a_functionB == None:
            a_functionB = a_functionA

        result = ParserResult()
        left = result.register(a_functionA())
        if result.error:
            return result

        while self.current_token.type in a_operations or (self.current_token.type, self.current_token.value) in a_operations:
            operator = self.current_token
            result.register_advancement()
            self.advance()
            right = result.register(a_functionB())
            if result.error:
                return result
            left = BinaryOperationNode(left, operator, right)

        return result.success(left)