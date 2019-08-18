################################################################################
## TOKENS
################################################################################

class Token:
    def __init__(self, a_type, a_value=None, a_position_start=None, a_position_end=None):
        self.type = a_type
        self.value = a_value

        if a_position_start:
            self.position_start = a_position_start.copy()
            self.position_end = a_position_start.copy()
            self.position_end.advance()

        if a_position_end:
            self.position_end = a_position_end.copy()

    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'