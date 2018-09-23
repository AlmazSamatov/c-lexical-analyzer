import re
from src.operators import _dictionary as op_dict
from src.delimiters import _dictionary as del_dict


# Tool that helps preprocessor to handle a c code
class PreprocessorTool:
    iterator = -1
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
        if type(iterator) is int:
            self.iterator = iterator

    # Moving iterator and getting new char
    def get_next_char(self):
        self.iterator += 1
        if self.iterator == len(self.c_code):
            return '_EOF'
        return self.c_code[self.iterator]

    def remove_first(self, string):
        self.c_code = self.c_code.replace(string, '', 1)

    def replace_all(self, replace_what, replace_to):
        all_d_quotes = self.find_all('"')
        all_replace_what = self.find_all(replace_what)
        while not len(all_replace_what) == 0:
            skip = False
            for i in range(0, len(all_d_quotes), 2):
                if all_replace_what[0] > all_d_quotes[i] and all_replace_what[0] < all_d_quotes[i+1]:
                    skip = True
                    all_replace_what.remove(all_replace_what[0])
            if all_replace_what[0] - 1 > -1 and (self.c_code[all_replace_what[0]-1] != ' ' and
                                                 self.c_code[all_replace_what[0]-1] != '\n' and
                                                 not self.c_code[all_replace_what[0]-1] in op_dict and
                                                 not self.c_code[all_replace_what[0]-1] in del_dict):
                skip = True
                all_replace_what.remove(all_replace_what[0])
            elif all_replace_what[0] + len(replace_what) < len(self.c_code) and \
                    (self.c_code[all_replace_what[0] + len(replace_what)] != ' ' and
                     self.c_code[all_replace_what[0] + len(replace_what)] != '\n' and
                     not self.c_code[all_replace_what[0] + len(replace_what)] in op_dict and
                     not self.c_code[all_replace_what[0] + len(replace_what)] in del_dict):
                skip = True
                all_replace_what.remove(all_replace_what[0])
            if not skip:
                self.c_code = self.c_code[:all_replace_what[0]] + replace_to + \
                              self.c_code[all_replace_what[0]+len(replace_what):]
                all_d_quotes = self.find_all('"')
                all_replace_what = self.find_all(replace_what)

    # Skips spaces
    def skip(self):
        while self.c_code[self.iterator + 1] == ' ':
            self.get_next_char()