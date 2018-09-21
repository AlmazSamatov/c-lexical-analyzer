def to_str(list):
    return ''.join(list)


def find_type(str):
    pass


def delete_comments(code):
    code = delete_oneline_comments(code)
    return delete_multiline_comments(code)


def delete_comments_universal(code, begin_str, end_str):
    indexes = []
    current_index = code.find(begin_str, 0)
    while current_index != -1:
        next_end_index = code.find(end_str, current_index)
        if next_end_index == -1:
            indexes.append((current_index, len(code) - 1))
        else:
            indexes.append((current_index, next_end_index + len(end_str) - 1))
        current_index = code.find('//', next_end_index)
    return delete_from_string_indexes(code, indexes)


def delete_oneline_comments(code):
    return delete_comments_universal(code, '//', '\n')


def delete_multiline_comments(code):
    return delete_comments_universal(code, '/*', '*/')


def delete_from_string_indexes(code, indexes):
    new_code = []
    curr_index = 0
    for i, (start, end) in enumerate(indexes):
        new_code.append(code[curr_index:start])
        curr_index = end + 1
        if i == len(indexes) - 1:
            new_code.append(code[curr_index:len(code)])
    return to_str(new_code)
