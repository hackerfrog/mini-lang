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