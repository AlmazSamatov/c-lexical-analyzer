from preprocessor_tool import PreprocessorTool


#  Starting all preprocessing tools
def start(c_code):
    replacing = scan_for_define(c_code)
    print('')


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


#  Maybe will have use in later...
# def replace_all(c_code, replace_what, replace_to):
#     preprocessor_tool = PreprocessorTool(c_code)
#     d_quote_open = False
#     current_char = preprocessor_tool.get_next_char()
#     if current_char != '_EOF':
#         if current_char == '"':
#             if d_quote_open:
#                 d_quote_open = False
#             else:
#                 d_quote_open = True
#         else:



