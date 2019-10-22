from mini.Tokenizer import *
from mini.Constants import *
from mini.Errors import *
from mini.Position import *

################################################################################
## LEXER
################################################################################

class Lexer:
    def __init__(self, a_file_name, a_text):
        self.file_name = a_file_name
        self.text = a_text
        self.current_position = Position(-1, 0, -1, a_file_name, a_text)
        self.current_character = None
        self.advance()

    def advance(self):
        self.current_position.advance(self.current_character)
        if self.current_position.index < len(self.text):
            self.current_character = self.text[self.current_position.index]
        else:
            self.current_character = None

    def make_tokens(self):
        tokens = list()

        while self.current_character != None:
            if self.current_character in ' \t':
                self.advance()
            elif self.current_character in DIGITS:
                tokens.append(self.make_number())
            elif self.current_character in LETTERS:
                tokens.append(self.make_identifier())
            elif self.current_character == '+':
                tokens.append(Token(TT_PLUS, a_position_start=self.current_position))
                self.advance()
            elif self.current_character == '-':
                tokens.append(Token(TT_MINUS, a_position_start=self.current_position))
                self.advance()
            elif self.current_character == '/':
                tokens.append(Token(TT_DIVIDE, a_position_start=self.current_position))
                self.advance()
            elif self.current_character == '%':
                tokens.append(Token(TT_MOD, a_position_start=self.current_position))
                self.advance()
            elif self.current_character == '(':
                tokens.append(Token(TT_L_PAREN, a_position_start=self.current_position))
                self.advance()
            elif self.current_character == ')':
                tokens.append(Token(TT_R_PAREN, a_position_start=self.current_position))
                self.advance()
            elif self.current_character == '~':
                tokens.append(Token(TT_BIT_NOT, a_position_start=self.current_position))
                self.advance()
            elif self.current_character == '&':
                tokens.append(Token(TT_BIT_AND, a_position_start=self.current_position))
                self.advance()
            elif self.current_character == '^':
                tokens.append(Token(TT_BIT_XOR, a_position_start=self.current_position))
                self.advance()
            elif self.current_character == '|':
                tokens.append(Token(TT_BIT_OR, a_position_start=self.current_position))
                self.advance()
            elif self.current_character == '*':
                tokens.append(self.make_astrict_operators())
            elif self.current_character == '!':
                token, error = self.make_notEqual_operator()
                if error:
                    return [], error
                tokens.append(token)
            elif self.current_character == '=':
                tokens.append(self.make_equals_operators())
            elif self.current_character == '<':
                tokens.append(self.make_lessThan_operators())
            elif self.current_character == '>':
                tokens.append(self.make_greaterThan_operators())
            else:
                position_start = self.current_position.copy()
                character = self.current_character
                self.advance()
                return [], IllegalCharacterError(position_start, self.current_position, f"'{character}'")

        tokens.append(Token(TT_EOF, a_position_start=self.current_position))
        return tokens, None

    def make_number(self):
        number_str = ''
        dot_count = 0
        position_start = self.current_position.copy()

        while self.current_character != None and self.current_character in DIGITS + '.':
            if self.current_character == '.':
                if dot_count == 1:
                    break

                dot_count += 1
                number_str += self.current_character
            else:
                number_str += self.current_character
            self.advance()

        if dot_count == 0:
            return Token(TT_INT, int(number_str), position_start, self.current_position)
        else:
            return Token(TT_FLOAT, float(number_str), position_start, self.current_position)

    def make_identifier(self):
        identifer = ''
        position_start = self.current_position.copy()

        while self.current_character != None and self.current_character in LETTERS_DIGITS + '_':
            identifer += self.current_character
            self.advance()

        token_type = TT_KEYWORD if identifer in KEYWORDS else TT_IDENTIFIER
        return Token(token_type, identifer, position_start, self.current_position)

    def make_astrict_operators(self):
        operator = ''
        position_start = self.current_position.copy()

        if self.current_character == '*':
            operator += self.current_character
        self.advance()

        if self.current_character == '*':
            operator += self.current_character
            self.advance()

        if operator == '*':
            return Token(TT_MULTIPLY, a_position_start=position_start)
        elif operator == '**':
            return Token(TT_POWER, a_position_start=position_start, a_position_end=self.current_position)

    def make_notEqual_operator(self):
        position_start = self.current_position.copy()
        self.advance()

        if self.current_character == '=':
            self.advance()
            return Token(TT_NOT_EQUAL, a_position_start=position_start, a_position_end=self.current_position), None

        self.advance()
        return None, ExpectedCharacterError(position_start, self.current_position, "'=' (after !)")

    def make_equals_operators(self):
        token_type = TT_EQUAL
        position_start = self.current_position.copy()
        self.advance()

        if self.current_character == '=':
            self.advance()
            token_type = TT_DOUBLE_EQUAL

        return Token(token_type, a_position_start=position_start, a_position_end=self.current_position)

    def make_lessThan_operators(self):
        token_type = TT_LESS_THAN
        position_start = self.current_position.copy()
        self.advance()

        if self.current_character == '<':
            self.advance()
            token_type = TT_LSHIFT
        elif self.current_character == '=':
            self.advance()
            token_type = TT_LESS_THAN_EQUAL

        return Token(token_type, a_position_start=position_start, a_position_end=self.current_position)

    def make_greaterThan_operators(self):
        token_type = TT_GREATER_THAN
        position_start = self.current_position.copy()
        self.advance()

        if self.current_character == '>':
            self.advance()
            token_type = TT_RSHIFT
        elif self.current_character == '=':
            self.advance()
            token_type = TT_GREATER_THAN_EQUAL

        return Token(token_type, a_position_start=position_start, a_position_end=self.current_position)