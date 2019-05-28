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
        return result

class IllegalCharacterError(Error):
    def __init__(self, a_position_start, a_position_end, a_details):
        super().__init__(a_position_start, a_position_end, 'Illegal Character', a_details)