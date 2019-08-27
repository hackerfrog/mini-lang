################################################################################
## NODES
################################################################################

class NumberNode:
    def __init__(self, a_token):
        self.token = a_token

    def __repr__(self):
        return f'{self.token}'

class BinaryOperationNode:
    def __init__(self, a_left, a_operator, a_right):
        self.left = a_left
        self.operator = a_operator
        self.right = a_right

    def __repr__(self):
        return f'({self.left}, {self.operator}, {self.right})'

class UnaryOperationNode:
    def __init__(self, a_operator, a_node):
        self.operator = a_operator
        self.node = a_node

    def __repr__(self):
        return f'({self.operator}, {self.node})'