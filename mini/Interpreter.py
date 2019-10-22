from mini.Constants import *
from mini.Values import *
from mini.Result import *

################################################################################
## INTERPRETER
################################################################################

class Interpreter:
    def visit(self, a_context, a_node):
        method_name = f'visit_{type(a_node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(a_context, a_node)

    def no_visit_method(self, a_context, a_node):
        raise Exception(f'No visit_{type(a_node).__name__} method defined')

    ## VISIT METHODS ###########################################################

    def visit_NumberNode(self, a_context, a_node):
        return RunTimeResult().success(
            Number(a_node.token.value).set_context(a_context).set_position(a_node.position_start, a_node.position_end)
        )

    def visit_VariableAccessNode(self, a_context, a_node):
        response = RunTimeResult()
        variable = a_node.variable.value
        value = a_context.symbol_table.get(variable)

        if not value:
            return response.failure(RunTimeError(
                a_context,
                a_node.position_start, a_node.position_end,
                f"'{variable}' is not defined"
            ))

        value = value.copy().set_position(a_node.position_start, a_node.position_end)
        return response.success(value)

    def visit_VariableAssignNode(self, a_context, a_node):
        response = RunTimeResult()
        variable = a_node.variable.value
        value = response.register(self.visit(a_context, a_node.value))
        if response.error:
            return response

        a_context.symbol_table.set(variable, value)
        return response.success(value)

    def visit_BinaryOperationNode(self, a_context, a_node):
        response = RunTimeResult()
        left = response.register(self.visit(a_context, a_node.left))
        if response.error:
            return response
        right = response.register(self.visit(a_context, a_node.right))
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
        elif a_node.operator.type == TT_MOD:
            result, error = left.mod_by(right)
        elif a_node.operator.type == TT_POWER:
            result, error = left.power_by(right)
        elif a_node.operator.type == TT_LSHIFT:
            result, error = left.leftShift_by(right)
        elif a_node.operator.type == TT_RSHIFT:
            result, error = left.rightShift_by(right)
        elif a_node.operator.type == TT_BIT_AND:
            result, error = left.bitAnd_by(right)
        elif a_node.operator.type == TT_BIT_XOR:
            result, error = left.bitXor_by(right)
        elif a_node.operator.type == TT_BIT_OR:
            result, error = left.bitOr_by(right)
        elif a_node.operator.type == TT_DOUBLE_EQUAL:
            result, error = left.doubleEqual_by(right)
        elif a_node.operator.type == TT_NOT_EQUAL:
            result, error = left.notEqual_by(right)
        elif a_node.operator.type == TT_LESS_THAN:
            result, error = left.lessThan_by(right)
        elif a_node.operator.type == TT_GREATER_THAN:
            result, error = left.greaterThan_by(right)
        elif a_node.operator.type == TT_LESS_THAN_EQUAL:
            result, error = left.lessThanEqual_by(right)
        elif a_node.operator.type == TT_GREATER_THAN_EQUAL:
            result, error = left.greaterThanEqual_by(right)
        elif a_node.operator.matches(TT_KEYWORD, 'AND'):
            result, error = left.boolAnd_by(right)
        elif a_node.operator.matches(TT_KEYWORD, 'OR'):
            result, error = left.boolOr_by(right)

        if error:
            return response.failure(error)
        else:
            return response.success(result.set_position(a_node.position_start, a_node.position_end))

    def visit_UnaryOperationNode(self, a_context, a_node):
        response = RunTimeResult()
        number = response.register(self.visit(a_context, a_node.node))
        if response.error:
            return response

        error = None

        if a_node.operator.type == TT_MINUS:
            number, error = number.multiply_by(Number(-1))
        elif a_node.operator.type == TT_BIT_NOT:
            number, error = number.bitNot_by()
        elif a_node.operator.matches(TT_KEYWORD, 'NOT'):
            number, error = number.boolNot_by()

        if error:
            return response.failure(error)
        else:
            return response.success(number.set_position(a_node.position_start, a_node.position_end))