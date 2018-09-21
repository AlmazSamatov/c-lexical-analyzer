from util import to_str, find_type, delete_comments, is_delimiter, is_operator


def scan(input_code):
    tokens = []

    input_code = delete_comments(input_code)
    input_code = input_code.replace('\n', ' ')
    current_index = 0
    char_list = []

    while len(char_list) > 0 or current_index < len(input_code):
        operator_lexeme = ''

        if current_index + 2 < len(input_code) and is_operator(input_code[current_index: current_index + 3]):
            # if we have operators as <<= etc.
            operator_lexeme = input_code[current_index: current_index + 3]
            # increment current index to operator length
            current_index += 3

        elif current_index + 1 < len(input_code) and is_operator(input_code[current_index: current_index + 2]):
            # if we have operators as ++, --, -> etc.
            operator_lexeme = input_code[current_index: current_index + 2]
            # increment current index to operator length
            current_index += 2

        elif current_index < len(input_code) and is_operator(input_code[current_index]):
            # if we have operators as +, -, {, } etc.
            operator_lexeme = input_code[current_index]
            # increment current index to operator length
            current_index += 1

        elif current_index < len(input_code) and not is_delimiter(input_code[current_index]):
            char_list.append(input_code[current_index])
            current_index += 1

        else:

            if len(char_list) > 0:
                current_lexeme = to_str(char_list)
                tokens.append((current_lexeme, find_type(current_lexeme)))
                char_list.clear()

            # add to tokens delimiter except whitespace
            if current_index < len(input_code) and input_code[current_index] != ' ':
                tokens.append((input_code[current_index], find_type(input_code[current_index])))

            current_index += 1

        # when we are go out of input code, but still have lexemes in char_list
        if current_index >= len(input_code) and len(char_list) > 0:
            current_lexeme = to_str(char_list)
            tokens.append((current_lexeme, find_type(current_lexeme)))
            char_list.clear()

        # if we found operator then initially put into the list our lexeme that ends in this index and after put operator
        if len(char_list) > 0 and len(operator_lexeme) > 0:
            # put some lexeme before operator
            current_lexeme = to_str(char_list)
            tokens.append((current_lexeme, find_type(current_lexeme)))
            char_list.clear()

            # put operator after lexeme
            tokens.append((operator_lexeme, find_type(operator_lexeme)))

    return tokens
