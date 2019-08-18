################################################################################
## POSITION
################################################################################

class Position:
    def __init__(self, a_index, a_line, a_column, a_file_name, a_file_text):
        self.index = a_index
        self.line = a_line
        self.column = a_column
        self.file_name = a_file_name
        self.file_text = a_file_text

    def advance(self, a_current_character=None):
        self.index += 1
        self.column += 1

        if a_current_character == '\n':
            self.line += 1
            self.column = 0

        return self

    def copy(self):
        return Position(self.index, self.line, self.column, self.file_name, self.file_text)