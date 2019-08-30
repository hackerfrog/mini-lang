from mini.Constants import *
from mini.Values import *

################################################################################
## INTERPRETER
################################################################################

class Interpreter:
    def visit(self, a_node):
        method_name = f'visit_{type(a_node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(a_node)

    def no_visit_method(self, a_node):
        raise Exception(f'No visit_{type(a_node).__name__} method defined')

    ## VISIT METHODS ###########################################################

    def visit_NumberNode(self, a_node):
        return Number(a_node.token.value).set_position(a_node.position_start, a_node.position_end)

    def visit_BinaryOperationNode(self, a_node):
        left = self.visit(a_node.left)
        right = self.visit(a_node.right)

        if a_node.operator.type == TT_PLUS:
            result = left.addition_by(right)
        elif a_node.operator.type == TT_MINUS:
            result = left.subtraction_by(right)
        elif a_node.operator.type == TT_MULTIPLY:
            result = left.multiply_by(right)
        elif a_node.operator.type == TT_DIVIDE:
            result = left.division_by(right)

        return result.set_position(a_node.position_start, a_node.position_end)

    def visit_UnaryOperationNode(self, a_node):
        number = self.visit(a_node.node)

        if a_node.operator.type == TT_MINUS:
            number = number.multiply_by(Number(-1))

        return number.set_position(a_node.position_start, a_node.position_end)