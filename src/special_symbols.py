_NEW_LINE = 87 # \n
_ALERT = 88 # \a
_BACKSPACE = 89 # \b
_CARRIAGE_RETURN = 90 # \r
_HORIZONTAL_TAB = 91 # \t
_VERTICAL_TAB = 92 # \v
_BACKSLASH = 93 # \\
_SINGLE_QUOTE = 94 # \'
_DOUBLE_QUOTE = 95 # \"
_QUESTION_MARK = 96 # \?
_FORM_FEED = 97 # \f

# Dictionary that correlates lexeme with token
_dictionary = {
    '\a': _ALERT,
    '\b': _BACKSPACE,
    '\f': _FORM_FEED,
    '\n': _NEW_LINE,
    '\t': _HORIZONTAL_TAB,
    '\v': _VERTICAL_TAB,
    '\\': _BACKSLASH,
    '\'': _SINGLE_QUOTE,
    '\"': _DOUBLE_QUOTE,
    '\?': _QUESTION_MARK
}