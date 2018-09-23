from preprocessor_tool import PreprocessorTool


#  Starting all preprocessing tools
def start(c_code):
    replacing = scan_for_define(c_code)
    for key, value in replacing.items():
        c_code = replace_all(c_code, key, value)
    return c_code

#  Scanning all '#define ' and return dictionary with format:
#  what_to_replace: on_what_to_replace
def scan_for_define(c_code):
    replacing = {}
    preprocessor_tool = PreprocessorTool(c_code)
    define_indexes = preprocessor_tool.find_all("#define ")
    for define_index in define_indexes:
        preprocessor_tool.set_iterator(define_index+7)
        preprocessor_tool.skip()
        replace_what = ''
        current_char = preprocessor_tool.get_next_char()
        if current_char == '_EOF':
            return replacing
        while current_char != ' ' and current_char != '\n':
            replace_what += current_char
            current_char = preprocessor_tool.get_next_char()
            if current_char == '_EOF':
                return replacing
        preprocessor_tool.skip()
        replace_to = ''
        current_char = preprocessor_tool.get_next_char()
        if current_char == '_EOF':
            return replacing
        while current_char != ' ' and current_char != '\n':
            replace_to += current_char
            current_char = preprocessor_tool.get_next_char()
            if current_char == '_EOF':
                replacing[replace_what] = replace_to
                return replacing
        replacing[replace_what] = replace_to
    return replacing


def replace_all(c_code, replace_what, replace_to):
    preprocessor_tool = PreprocessorTool(c_code)
    define_string = '#define ' + replace_what + ' ' + replace_to
    preprocessor_tool.remove_first(define_string)
    preprocessor_tool.replace_all(replace_what, replace_to)
    return preprocessor_tool.c_code
