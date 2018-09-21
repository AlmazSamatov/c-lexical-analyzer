import keywords
import delimiters
import general_tokens
import operators
from util import to_str
from util import find_type
from util import delete_comments


def scan(input_code):
    tokens = []

    input_code = delete_comments(input_code)
    input_code = input_code.replace('\n', ' ')
    current_index = 0
    char_list = []

    while len(char_list) > 0 or current_index < len(input_code):

        if current_index < len(input_code) and not is_delimiter(input_code[current_index]):
            char_list.append(input_code[current_index])
        elif len(char_list) > 0:
            current_lexeme = to_str(char_list)
            type_of_lexeme = int()

            if is_operator(current_lexeme):
                type_of_lexeme = find_type(current_lexeme)
            elif is_keyword(current_lexeme):
                type_of_lexeme = find_type(current_lexeme)
            elif is_int(current_lexeme):
                type_of_lexeme = general_tokens._NUM
            elif is_real_num(current_lexeme):
                type_of_lexeme = general_tokens._REAL
            elif is_string(current_lexeme):
                type_of_lexeme = general_tokens._STRING
            elif is_char(current_lexeme):
                type_of_lexeme = general_tokens._CHAR
            elif is_identifier(current_lexeme):
                type_of_lexeme = general_tokens._IDENTIFIER
            else:
                type_of_lexeme = general_tokens._ERROR

            tokens.append((current_lexeme, type_of_lexeme))
            char_list.clear()

        current_index += 1

    return tokens


def is_operator(lexeme):
    # + - = / *
    return operators._dictionary.get(lexeme) != None


def is_string(lexeme):
    # begins with " and ends with "
    return lexeme[0] == '"' and lexeme[len(lexeme) - 1] == '"'


def is_char(lexeme):
    # begins with ' and ends with ' and length is 3
    return len(lexeme) == 3 and lexeme[0] == "'" and lexeme[2] == "'"


def is_keyword(lexeme):
    return keywords._dictionary.get(lexeme) != None


def is_identifier(lexeme):
    if lexeme[0] != '_' and not lexeme[0].isalpha():
        return False
    for char in lexeme:
        if not char.isdigit() and not char[0].isalpha() and char != '_':
            return False
    return True


def is_delimiter(lexeme):
    # , ; { } etc.
    return delimiters._dictionary.get(lexeme) != None


def is_int(lexeme):
    first = True
    for char in lexeme:
        if not char.isdigit() or (char == '-' and not first):
            return False
        first = False
    return True


def is_real_num(lexeme):
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
