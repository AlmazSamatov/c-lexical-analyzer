from src.delimiters import _dictionary as delimiters
from src.keywords import _dictionary as keywords
from src.operators import _dictionary as operators
import src.general_tokens as general_tokens


def to_str(list):
    """
    Converts list to string
    :param list: list that need to be converted
    :return: list converted into string
    """
    return ''.join(list)


def find_type(lexeme):
    """
    Determines type of the lexeme
    :param lexeme: input lexeme
    :return: type of the lexeme
    """
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
    """
    Checks if current lexeme is operator
    :param lexeme: input lexeme
    :return: True if the lexeme is operator, False otherwise
    """
    # + - = / *
    return operators.get(lexeme) != None


def is_string(lexeme):
    """
    Checks if current lexeme is string
    :param lexeme: input lexeme
    :return: True if the lexeme is string, False otherwise
    """
    # begins with " and ends with "
    return lexeme[0] == '"' and lexeme[len(lexeme) - 1] == '"'


def is_char(lexeme):
    """
    Checks if current lexeme is char
    :param lexeme: input lexeme
    :return: True if the lexeme is char, False otherwise
    """
    # begins with ' and ends with ' and length is 3
    return len(lexeme) == 3 and lexeme[0] == "'" and lexeme[2] == "'"


def is_keyword(lexeme):
    """
    Checks if current lexeme is keyword
    :param lexeme: input lexeme
    :return: True if the lexeme is keyword, False otherwise
    """
    return keywords.get(lexeme) != None


def is_identifier(lexeme):
    """
    Checks if current lexeme is identifier
    :param lexeme: input lexeme
    :return: True if the lexeme is identifier, False otherwise
    """
    if lexeme[0] != '_' and not lexeme[0].isalpha():
        return False
    for char in lexeme:
        if not char.isdigit() and not char[0].isalpha() and char != '_':
            return False
    return True


def is_delimiter(lexeme):
    """
    Checks if current lexeme is delimiter
    :param lexeme: input lexeme
    :return: True if the lexeme is delimiter, False otherwise
    """
    # , ; { } etc.
    return delimiters.get(lexeme) != None


def is_int(lexeme):
    """
    Checks if current lexeme is int
    :param lexeme: input lexeme
    :return: True if the lexeme is int, False otherwise
    """
    for i, char in enumerate(lexeme):
        if not char.isdigit() and not (char == '-' and i == 0):
            return False
    return True


def is_real_num(lexeme):
    """
    Checks if current lexeme is real number
    :param lexeme: input lexeme
    :return: True if the lexeme is real number, False otherwise
    """
    is_decimal = False
    for i, char in enumerate(lexeme):
        if not char.isdigit() and (char == '-' and i != 0):
            return False
        if char == '.' and not is_decimal:
            is_decimal = True
        elif char == '.' and is_decimal:
            return False
    return is_decimal
