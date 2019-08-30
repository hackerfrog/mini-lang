################################################################################
## NUMBER
################################################################################

class Number:
    def __init__(self, a_value):
        self.value = a_value
        self.set_position()

    def set_position(self, a_position_start=None, a_position_end=None):
        self.position_start = a_position_start
        self.position_end = a_position_end
        return self

    def addition_by(self, a_other):
        if isinstance(a_other, Number):
            return Number(self.value + a_other.value)

    def subtraction_by(self, a_other):
        if isinstance(a_other, Number):
            return Number(self.value - a_other.value)

    def multiply_by(self, a_other):
        if isinstance(a_other, Number):
            return Number(self.value * a_other.value)

    def division_by(self, a_other):
        if isinstance(a_other, Number):
            return Number(self.value / a_other.value)