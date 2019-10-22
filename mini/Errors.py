from mini.error_pointer import *

################################################################################
## ERRORS
################################################################################

class Error:
    def __init__(self, a_position_start, a_position_end, a_error_name, a_details):
        self.position_start = a_position_start
        self.position_end = a_position_end
        self.error_name = a_error_name
        self.details = a_details

    def as_string(self):
        result = f'{self.error_name}: {self.details}'
        result += f'\nFile: {self.position_start.file_name}, Line: {self.position_start.line + 1}, Column: {self.position_start.column + 1}'
        result += '\n\n' + error_pointer(self.position_start.file_text, self.position_start, self.position_end)
        return result

class IllegalCharacterError(Error):
    def __init__(self, a_position_start, a_position_end, a_details):
        super().__init__(a_position_start, a_position_end, 'Illegal Character', a_details)

class ExpectedCharacterError(Error):
    def __init__(self, a_position_start, a_position_end, a_details):
        super().__init__(a_position_start, a_position_end, 'Expected Character', a_details)

class InvalidSyntaxError(Error):
    def __init__(self, a_position_start, a_position_end, a_details=''):
        super().__init__(a_position_start, a_position_end, 'Invalid Syntax', a_details)

class RunTimeError(Error):
    def __init__(self, a_context, a_position_start, a_position_end, a_details=''):
        super().__init__(a_position_start, a_position_end, 'Run Time Error', a_details)
        self.context = a_context

    def as_string(self):
        result = self.traceback()
        result += f'{self.error_name}: {self.details}'
        result += '\n\n' + error_pointer(self.position_start.file_text, self.position_start, self.position_end)
        return result

    def traceback(self):
        result = ''
        position = self.position_start
        context = self.context

        while context:
            result = f'    File: {position.file_name}, Line: {position.line + 1}, in {context.display_name}\n' + result
            position = context.parent_entry_position
            context = context.parent

        return 'Traceback (most recent call last):\n' + result