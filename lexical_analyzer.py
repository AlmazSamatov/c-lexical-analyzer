import constants
from util import to_str
from util import find_type


def scan(input_code):
    current_index = 0
    char_list = []

    while len(char_list) > 0 or current_index < len(input_code):

        current_lexeme = to_str(char_list)

        if not is_delimiter(input_code[current_index]):
            char_list.append(input_code[current_index])
            current_index += 1
        elif current_index + 1 < len(input_code) and is_operator(input_code[current_index: current_index + 2]):
            # if we have operators as ++, --, -> etc.
            print(find_type(input_code[current_index: current_index + 2]))
            current_index += 2
        elif is_operator(input_code[current_index]):
            # if we have operatores as +, -, {, } etc.
            print(find_type(input_code[current_index]))
            current_index += 1
        elif is_keyword(current_lexeme):
            print(find_type(current_lexeme))
        elif is_int(current_lexeme):
            print()
        elif is_real_num(current_lexeme):
            print()
        elif is_string(current_lexeme):
            print()
        elif is_identifier(current_lexeme):
            print()
        else:
            print()


def is_operator(str):
    # + - = / *
    pass


def is_keyword(str):
    pass


def is_identifier(str):
    pass


def is_string(str):
    # begins and ends with ", do not have " inside
    pass


def is_delimiter(str):
    # , ; { } etc.
    pass


def is_int(str):
    first = True
    for char in str:
        if not char.is_digit() or (char == '-' and not first):
            return False
        first = False
    return True


def is_real_num(str):
    first = True
    is_decimal = False
    for char in str:
        if not char.is_digit() or (char == '-' and not first):
            return False
        if char == '.' and not is_decimal:
            is_decimal = True
        elif char == '.' and is_decimal:
            return False
        first = False
    return is_decimal
