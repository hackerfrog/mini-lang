################################################################################
## NODES
################################################################################

class NumberNode:
    def __init__(self, a_token):
        self.token = a_token
        self.position_start = self.token.position_start
        self.position_end = self.token.position_end

    def __repr__(self):
        return f'{self.token}'

class VariableAccessNode:
    def __init__(self, a_variable):
        self.variable = a_variable
        self.position_start = self.variable.position_start
        self.position_end = self.variable.position_end

class VariableAssignNode:
    def __init__(self, a_variable, a_value):
        self.variable = a_variable
        self.value = a_value
        self.position_start = self.variable.position_start
        self.position_end = self.value.position_end

class BinaryOperationNode:
    def __init__(self, a_left, a_operator, a_right):
        self.left = a_left
        self.operator = a_operator
        self.right = a_right
        self.position_start = self.left.position_start
        self.position_end = self.right.position_end

    def __repr__(self):
        return f'({self.left}, {self.operator}, {self.right})'

class UnaryOperationNode:
    def __init__(self, a_operator, a_node):
        self.operator = a_operator
        self.node = a_node
        self.position_start = self.operator.position_start
        self.position_end = self.node.position_end

    def __repr__(self):
        return f'({self.operator}, {self.node})'

class IfElseNode:
    def __init__(self, a_cases, a_else_case):
        self.cases = a_cases
        self.else_case = a_else_case

        self.position_start = self.cases[0][0].position_start
        self.position_end = (self.else_case or self.cases[len(self.cases) - 1][0]).position_end