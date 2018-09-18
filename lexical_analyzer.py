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
    _MIN = 12  # -
    _DEC = 13  # --
    _MASSIGN = 13  # -=
    _DIV = 14  # /
    _MULASSIGN = 15 # *=
    input_code = ""
    iterator = -1

    def __init__(self, input_code):
        self.input_code = input_code

    def get_char_at_iterator(self):
        if self.iterator >= len(self.input_code):
            return None
        else:
            return self.input_code[self.iterator]
        
    def get_next(self):
        self.iterator += 1
        return self.get_char_at_iterator()

    def next_lex(self):
        c = self.get_next()
        while c == ' ':
            c = self.get_next()
        if c == ';':
            return self._SEMI
        if c is None:
            return self._EOF
        if c.isdigit():
            while c.isdigit():
                c = self.get_next()
            if c == ' ' or c == ";":
                self.iterator -= 1
                return self._NUM
            else:
                self.iterator -= 1
                return self._ERROR
        if c == '=':
            c = self.get_next()
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
            c = self.get_next()
            if c == '=':
                return self._MULASSIGN
            else:
                self.iterator -= 1
                return self._MUL
        if c == "&":
            return self._AND
        if c == '+':
            c = self.get_next()
            if c == '+':
                return self._INC
            elif c == '=':
                return self._PASSIGN
            else:
                self.iterator -= 1
                return self._PLUS
        if c == '-':
            c = self.get_next()
            if c == '-':
                return self._DEC
            elif c == '=':
                return self._MASSIGN
            else:
                self.iterator -= 1
                return self._MIN

    def scan(self):
        rez = self.next_lex()
        print(rez)
        while rez != 0:
            rez = self.next_lex()
            print(rez)

