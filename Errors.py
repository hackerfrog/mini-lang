################################################################################
## ERRORS
################################################################################

class Error:
    def __init__(self, a_error_name, a_details):
        self.error_name = a_error_name
        self.details = a_details
    
    def as_string(self):
        result = f'{self.error_name}: {self.details}'
        return result

class IllegalCharacterError(Error):
    def __init__(self, a_details):
        super().__init__('Illegal Character', a_details)