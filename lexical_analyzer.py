import keywords
import delimiters
import general_tokens
import operators
from util import to_str
from util import find_type
from util import delete_comments


def scan(input_code):
    input_code = delete_comments(input_code)
    current_index = 0
    char_list = []

    while len(char_list) > 0 or current_index < len(input_code):

        if not is_delimiter(input_code[current_index]):
            char_list.append(input_code[current_index])
            current_index += 1
        elif current_index + 2 < len(input_code) and is_operator(input_code[current_index: current_index + 3]):
            # if we have operators as <<= etc.
            print(find_type(input_code[current_index: current_index + 3]))
            current_index += 3
        elif current_index + 1 < len(input_code) and is_operator(input_code[current_index: current_index + 2]):
            # if we have operators as ++, --, -> etc.
            print(find_type(input_code[current_index: current_index + 2]))
            current_index += 2
        elif is_operator(input_code[current_index]):
            # if we have operatores as +, -, {, } etc.
            print(find_type(input_code[current_index]))
            current_index += 1
        else:
            current_lexeme = to_str(char_list)

            if is_keyword(current_lexeme):
                print(find_type(current_lexeme))
            elif is_int(current_lexeme):
                print(general_tokens._NUM)
            elif is_real_num(current_lexeme):
                print(general_tokens._REAL)
            elif is_string(current_lexeme):
                print()
            elif is_identifier(current_lexeme):
                print()
            else:
                print()
            char_list.clear()


def is_operator(str):
    # + - = / *
    return operators._dictionary.get(str) != None


def is_keyword(str):
    return keywords._dictionary.get(str) != None


def is_identifier(str):
    pass


def is_string(str):
    # begins and ends with ", do not have " inside
    pass


def is_char(str):
    pass
    # return len(str) == 3 and str[0] == "'" and str[2] == "'" and (str[1].isdigit() or str[1].is)


def is_delimiter(str):
    # , ; { } etc.
    return delimiters._dictionary.get(str) != None


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
