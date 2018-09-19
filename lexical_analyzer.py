import constants


class LexicalAnalyzer:
    input_code = ""

    def __init__(self, input_code):
        self.input_code = input_code

    def get_char(self, i):
        return self.input_code[i]

    def scan(self):
        left, right = 0, 0
        while left < right < len(self.input_code):
            pass
            # here will be parsing of input code

    def is_int(self, str):
        first = True
        for char in str:
            if not char.is_digit() or (char == '-' and not first):
                return False
            first = False
        return True

    def is_real_num(self, str):
        first = True
        is_decimal = False
        for char in str:
            if not char.is_digit() or (char == '-' and not first):
                return False
            if char == '.' and not is_decimal:
                is_decimal = True
            elif char == '.' and is_decimal:
                return False
            first = False
        return is_decimal
