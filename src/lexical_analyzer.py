from src import delimiters, general_tokens, keywords, operators
from src.util import to_str
from src.util import find_type
from src.util import delete_comments


def scan(input_code):
    tokens = []

    input_code = delete_comments(input_code)
    input_code = input_code.replace('\n', ' ')
    current_index = 0
    char_list = []

    while len(char_list) > 0 or current_index < len(input_code):
        operator_lexeme = ''
        operator_length = 0

        if current_index + 2 < len(input_code) and is_operator(input_code[current_index: current_index + 3]):
            # if we have operators as <<= etc.
            operator_lexeme = input_code[current_index: current_index + 3]
            operator_length = 3

        elif current_index + 1 < len(input_code) and is_operator(input_code[current_index: current_index + 2]):
            # if we have operators as ++, --, -> etc.
            operator_lexeme = input_code[current_index: current_index + 2]
            operator_length = 2

        elif current_index < len(input_code) and is_operator(input_code[current_index]):
            # if we have operators as +, -, {, } etc.
            operator_lexeme = input_code[current_index]
            operator_length = 1

        elif current_index < len(input_code) and not is_delimiter(input_code[current_index]):
            char_list.append(input_code[current_index])

        elif len(char_list) > 0:
            current_lexeme = to_str(char_list)
            tokens.append((current_lexeme, find_type_of_lexeme(current_lexeme)))
            char_list.clear()

        # if we found operator then initially put into the list our lexeme that ends in this index and after put operator
        if len(char_list) > 0 and len(operator_lexeme) > 0:
            # put some lexeme before operator
            current_lexeme = to_str(char_list)
            tokens.append((current_lexeme, find_type_of_lexeme(current_lexeme)))
            char_list.clear()

            # put operator after lexeme
            tokens.append((operator_lexeme, find_type_of_lexeme(operator_lexeme)))
            current_index += operator_length - 1  # minus 1, because at the end we increment current index to 1

        current_index += 1

    return tokens


def find_type_of_lexeme(lexeme):
    type_of_lexeme = int()

    if is_keyword(lexeme):
        type_of_lexeme = find_type(lexeme)
    elif is_int(lexeme):
        type_of_lexeme = general_tokens._NUM
    elif is_real_num(lexeme):
        type_of_lexeme = general_tokens._REAL
    elif is_string(lexeme):
        type_of_lexeme = general_tokens._STRING
    elif is_char(lexeme):
        type_of_lexeme = general_tokens._CHAR
    elif is_identifier(lexeme):
        type_of_lexeme = general_tokens._IDENTIFIER
    else:
        type_of_lexeme = general_tokens._ERROR

    return type_of_lexeme


def is_operator(lexeme):
    # + - = / *
    if not type(lexeme) is str:
        return False
    return operators._dictionary.get(lexeme) != None


def is_string(lexeme):
    # begins with " and ends with "
    if not type(lexeme) is str:
        return False
    return lexeme[0] == '"' and lexeme[len(lexeme) - 1] == '"'


def is_char(lexeme):
    # begins with ' and ends with ' and length is 3
    if not type(lexeme) is str:
        return False
    return len(lexeme) == 3 and lexeme[0] == "'" and lexeme[2] == "'"


def is_keyword(lexeme):
    if not type(lexeme) is str:
        return False
    return keywords._dictionary.get(lexeme) != None


def is_identifier(lexeme):
    if not type(lexeme) is str:
        return False
    if lexeme[0] != '_' and not lexeme[0].isalpha():
        return False
    for char in lexeme:
        if not char.isdigit() and not char[0].isalpha() and char != '_':
            return False
    return True


def is_delimiter(lexeme):
    # , ; { } etc.
    if not type(lexeme) is str:
        return False
    return delimiters._dictionary.get(lexeme) != None


def is_int(lexeme):
    if not type(lexeme) is str:
        return False
    first = True
    for char in lexeme:
        if not char.isdigit() or (char == '-' and not first):
            return False
        first = False
    return True


def is_real_num(lexeme):
    if not type(lexeme) is str:
        return False
    first = True
    is_decimal = False
    for char in lexeme:
        if not char.isdigit() or (char == '-' and not first):
            return False
        if char == '.' and not is_decimal:
            is_decimal = True
        elif char == '.' and is_decimal:
            return False
        first = False
    return is_decimal
