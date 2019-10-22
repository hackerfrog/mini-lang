from mini.Errors import *

################################################################################
## NUMBER
################################################################################

class Number:
    def __init__(self, a_value):
        self.value = a_value
        self.set_position()
        self.set_context()

    def set_position(self, a_position_start=None, a_position_end=None):
        self.position_start = a_position_start
        self.position_end = a_position_end
        return self

    def set_context(self, a_context=None):
        self.context = a_context
        return self

    def addition_by(self, a_other):
        if isinstance(a_other, Number):
            return Number(self.value + a_other.value).set_context(self.context), None

    def subtraction_by(self, a_other):
        if isinstance(a_other, Number):
            return Number(self.value - a_other.value).set_context(self.context), None

    def multiply_by(self, a_other):
        if isinstance(a_other, Number):
            return Number(self.value * a_other.value).set_context(self.context), None

    def division_by(self, a_other):
        if isinstance(a_other, Number):
            if a_other.value == 0:
                return None, RunTimeError(
                    self.context,
                    a_other.position_start, a_other.position_end,
                    'Division by zero'
                )
            return Number(self.value / a_other.value).set_context(self.context), None

    def mod_by(self, a_other):
        if isinstance(a_other, Number):
            if a_other.value == 0:
                return None, RunTimeError(
                    self.context,
                    a_other.position_start, a_other.position_end,
                    'Mod by zero'
                )
            return Number(self.value % a_other.value).set_context(self.context), None

    def power_by(self, a_other):
        if isinstance(a_other, Number):
            return Number(self.value ** a_other.value).set_context(self.context), None

    def leftShift_by(self, a_other):
        if isinstance(a_other, Number):
            if a_other.value < 0:
                return None, RunTimeError(
                    self.context,
                    a_other.position_start, a_other.position_end,
                    'Negative shift'
                )
            return Number(self.value << a_other.value).set_context(self.context), None

    def rightShift_by(self, a_other):
        if isinstance(a_other, Number):
            if a_other.value < 0:
                return None, RunTimeError(
                    self.context,
                    a_other.position_start, a_other.position_end,
                    'Negative shift'
                )
            return Number(self.value >> a_other.value).set_context(self.context), None

    def bitNot_by(self):
        return Number(~(self.value)).set_context(self.context), None

    def bitAnd_by(self, a_other):
        if isinstance(a_other, Number):
            return Number(self.value & a_other.value).set_context(self.context), None

    def bitXor_by(self, a_other):
        if isinstance(a_other, Number):
            return Number(self.value ^ a_other.value).set_context(self.context), None

    def bitOr_by(self, a_other):
        if isinstance(a_other, Number):
            return Number(self.value | a_other.value).set_context(self.context), None

    def copy(self):
        copy = Number(self.value)
        copy.set_position(self.position_start, self.position_end)
        copy.set_context(self.context)
        return copy

    def __repr__(self):
        return str(self.value)