from mini.Constants import *
from mini.Values import *
from mini.Result import *

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
        return RunTimeResult().success(
            Number(a_node.token.value).set_position(a_node.position_start, a_node.position_end)
        )

    def visit_BinaryOperationNode(self, a_node):
        response = RunTimeResult()
        left = response.register(self.visit(a_node.left))
        if response.error:
            return response
        right = response.register(self.visit(a_node.right))
        if response.error:
            return response

        if a_node.operator.type == TT_PLUS:
            result, error = left.addition_by(right)
        elif a_node.operator.type == TT_MINUS:
            result, error = left.subtraction_by(right)
        elif a_node.operator.type == TT_MULTIPLY:
            result, error = left.multiply_by(right)
        elif a_node.operator.type == TT_DIVIDE:
            result, error = left.division_by(right)

        if error:
            return response.failure(error)
        else:
            return response.success(result.set_position(a_node.position_start, a_node.position_end))

    def visit_UnaryOperationNode(self, a_node):
        response = RunTimeResult()
        number = response.register(self.visit(a_node.node))
        if response.error:
            return response

        error = None

        if a_node.operator.type == TT_MINUS:
            number, error = number.multiply_by(Number(-1))

        if error:
            return response.failure(error)
        else:
            return response.success(number.set_position(a_node.position_start, a_node.position_end))