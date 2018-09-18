import constants


class LexicalAnalyzer:
    input_code = ""
    iterator = -1

    def __init__(self, input_code):
        self.input_code = input_code

    def get_char_at_iterator(self):
        if self.iterator >= len(self.input_code):
            return None
        else:
            return self.input_code[self.iterator]

    def next_lex(self):
        self.iterator += 1
        c = self.get_char_at_iterator()
        while c == ' ':
            self.iterator += 1
            c = self.get_char_at_iterator()
        if c == ';':
            return constants._SEMI
        if c is None:
            return self._EOF
        if c.isdigit():
            while c.isdigit():
                self.iterator += 1
                c = self.get_char_at_iterator()
            if c == ' ' or c == ";":
                self.iterator -= 1
                return constants._NUM
            else:
                self.iterator -= 1
                return constants._ERROR
        if c == '=':
            self.iterator += 1
            c = self.get_char_at_iterator()
            if c == '=':
                return constants._EQUAL
            else:
                self.iterator -= 1
                return constants._ASSIGN
        if c == '(':
            return constants._LP
        if c == ')':
            return constants._RP
        if c == '*':
            self.iterator += 1
            c = self.get_char_at_iterator()
            if c == '=':
                return constants._MULASSIGN
            else:
                self.iterator -= 1
                return constants._MUL
        if c == "&":
            return constants._AND
        if c == '+':
            self.iterator += 1
            c = self.get_char_at_iterator()
            if c == '+':
                return constants._INC
            elif c == '=':
                return constants._PASSIGN
            else:
                self.iterator -= 1
                return constants._PLUS
        if c == '-':
            self.iterator += 1
            c = self.get_char_at_iterator()
            if c == '-':
                return constants._DEC
            elif c == '=':
                return constants._MASSIGN
            else:
                self.iterator -= 1
                return constants._MIN

    def scan(self):
        rez = self.next_lex()
        print(rez)
        while rez != 0:
            rez = self.next_lex()
            print(rez)
