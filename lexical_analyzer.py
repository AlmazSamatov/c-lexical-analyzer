class LexicalAnalyzer:
    _ERROR = -1  # Unknown lex
    _NUM = 1  # Some digit
    _EOF = 0  # End of file
    _SEMI = 2  # ;
    _EQUAL = 3  # ==
    _ASSIGN = 4  # =
    _LP = 5  # (
    _RP = 6  # )
    _MUL = 7  # *
    _AND = 8  # &
    _PLUS = 9  # +
    _INC = 10  # ++
    _PASSIGN = 11  # +=
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
        if c == ';':
            return self._SEMI
        if c is None:
            return self._EOF
        if c.isdigit():
            while c.isdigit():
                self.iterator += 1
                c = self.get_char_at_iterator()
            if c != ' ' and c != ";":
                self.iterator -= 1
                return self._ERROR
            else:
                self.iterator -= 1
                return self._NUM
        if c == '=':
            self.iterator += 1
            c = self.get_char_at_iterator()
            if c == '=':
                return self._EQUAL
            else:
                self.iterator -= 1
                return self._ASSIGN
        if c == '(':
            return  self._LP
        if c == ')':
            return self._RP
        if c == '*':
            return self._MUL
        if c == "&":
            return self._AND
        if c == '+':
            self.iterator += 1
            c = self.get_char_at_iterator()
            if c == '+':
                return self._INC
            elif c == '=':
                return self._PASSIGN


    def scan(self):
        rez = self.next_lex()
        print(rez)
        while rez != 0:
            rez = self.next_lex()
            print(rez)

