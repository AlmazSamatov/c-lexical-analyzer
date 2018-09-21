import re


# Tool that helps preprocessor to handle a c code
class PreprocessorTool:
    iterator = 0
    c_code = ''

    # Constructor with c code as a parameter
    def __init__(self, c_code):
        self.c_code = c_code

    # Finding first entry of a string in the c code
    def find(self, string):
        return self.c_code.find(string)

    # Finding all entries of a string and returns it as a list
    def find_all(self, string):
        return [m.start() for m in re.finditer(string, self.c_code)]

    # Set iterator of a preprocessor tool
    def set_iterator(self, iterator):
        self.iterator = iterator

    # Moving iterator and getting new char
    def get_next_char(self):
        self.iterator += 1
        if self.iterator == len(self.c_code):
            return '_EOF'
        return self.c_code[self.iterator]

    # Skips spaces
    def skip(self):
        while self.c_code[self.iterator + 1] == ' ':
            self.get_next_char()