from src.delimiters import _dictionary as delimiters
from src.keywords import _dictionary as keywords
from src.operators import _dictionary as operators
import src.general_tokens as general_tokens


def to_str(list):
    return ''.join(list)


def find_type(lexeme):
    types = []
    types.append(delimiters.get(lexeme))
    types.append(keywords.get(lexeme))
    types.append(operators.get(lexeme))
    for type in types:
        if type != None:
            return type
    if is_int(lexeme):
        return general_tokens._NUM
    elif is_real_num(lexeme):
        return general_tokens._REAL
    elif is_string(lexeme):
        return general_tokens._STRING
    elif is_char(lexeme):
        return general_tokens._CHAR
    elif is_identifier(lexeme):
        return general_tokens._IDENTIFIER
    else:
        return general_tokens._ERROR


def is_operator(lexeme):
    # + - = / *
    return operators.get(lexeme) != None


def is_string(lexeme):
    # begins with " and ends with "
    return lexeme[0] == '"' and lexeme[len(lexeme) - 1] == '"'


def is_char(lexeme):
    # begins with ' and ends with ' and length is 3
    return len(lexeme) == 3 and lexeme[0] == "'" and lexeme[2] == "'"


def is_keyword(lexeme):
    return keywords.get(lexeme) != None


def is_identifier(lexeme):
    if lexeme[0] != '_' and not lexeme[0].isalpha():
        return False
    for char in lexeme:
        if not char.isdigit() and not char[0].isalpha() and char != '_':
            return False
    return True


def is_delimiter(lexeme):
    # , ; { } etc.
    return delimiters.get(lexeme) != None


def is_int(lexeme):
    for i, char in enumerate(lexeme):
        if not char.isdigit() or (char == '-' and i != 0):
            return False
    return True


def is_real_num(lexeme):
    is_decimal = False
    for i, char in enumerate(lexeme):
        if not char.isdigit() and (char == '-' and i != 0):
            return False
        if char == '.' and not is_decimal:
            is_decimal = True
        elif char == '.' and is_decimal:
            return False
    return is_decimal
