from preprocessor_tool import PreprocessorTool


def start(c_code):
    replace_what, replace_to = scan_for_define(c_code)
    print('')


def scan_for_define(c_code):
    preprocessor_tool = PreprocessorTool(c_code)
    define_index = preprocessor_tool.find('#define ')
    if define_index != -1:
        preprocessor_tool.set_iterator(define_index+7)
        preprocessor_tool.skip(' ')
        replace_what = ''
        current_char = preprocessor_tool.get_next_char()
        if current_char == '_EOF':
            return None
        while current_char != ' ':
            replace_what += current_char
            current_char = preprocessor_tool.get_next_char()
            if current_char == '_EOF':
                return None
        preprocessor_tool.skip(' ')
        replace_to = ''
        current_char = preprocessor_tool.get_next_char()
        if current_char == '_EOF':
            return None
        while current_char != ' ':
            replace_to += current_char
            current_char = preprocessor_tool.get_next_char()
            if current_char == '_EOF':
                return replace_what, replace_to
        return replace_what, replace_to
    return None, None


def replace_all(c_code, replace_what, replace_to):
    preprocessor_tool = PreprocessorTool(c_code)
    d_quote_open = False
    current_char = preprocessor_tool.get_next_char()
    if current_char != '_EOF':
        if current_char == '"':
            if d_quote_open:
                d_quote_open = False
            else:
                d_quote_open = True
        else:



