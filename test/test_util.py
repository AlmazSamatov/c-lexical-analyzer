from src.util import *


def test_to_str():
    assert to_str(['777', 'is that the best c lexer?', 'True']) == '777is that the best c lexer?True'


def test_1_find_type():
    assert find_type(';') == 85


def test_2_find_type():
    assert find_type('-2sd;3') is None


def test_3_find_type():
    assert find_type('+') == 2


def test_delete_from_string_indexes():
    #  todo: idk what the purpose of the function is, so test will be written l8r
    pass


def test_delete_multiline_comments():
    in_c = '/* this \n is \n very \n big \n comment*/'
    assert delete_multiline_comments(in_c) == ''


def test_oneline_comment():
    in_c = '// Simple comment that says it should be deleted'
    assert delete_oneline_comments(in_c) == ''


def test_delete_comments_universal():
    in_c = '#  what if comments start not like in c? \nHope this line isn\'t deleted'
    assert delete_comments_universal(in_c, '#', '\n') == 'Hope this line isn\'t deleted'


def test_delete_comments():
    in_c = '// HOLY COW!!! \n' \
           '/* THIS \nTHING \nCAN \nDELETE \nALL \nTYPES \nOF \nC \nCOMMENTS!'
    assert delete_comments(in_c) == ''
