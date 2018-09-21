class PreprocessorTool:
    iterator = 0
    c_code = ''

    def __init__(self, c_code):
        self.c_code = c_code


    def find(self, string):
        return self.c_code.find(string)

    def set_iterator(self, iterator):
        self.iterator = iterator

    def get_next_char(self):
        self.iterator += 1
        if self.iterator == len(self.c_code):
            return '_EOF'
        return self.c_code[self.iterator]

    def skip(self, string):
        while self.c_code[self.iterator + 1] == string:
            self.get_next_char()

    def delete_first(self):