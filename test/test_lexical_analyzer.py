from src.lexical_analyzer import *


def test_1_is_delimiter():
    assert is_delimiter('(') is True


def test_2_is_delimiter():
    assert is_delimiter('+') is False


def test_1_is_operator():
    assert is_operator('+') is True


def test_2_is_operator():
    assert is_operator('0') is False


def test_3_is_operator():
    assert is_operator(True) is False


def test_scan():
    in_c = '// user-defined function to check prime number \n\
            int checkPrimeNumber(int n) \n\
            { \n\
                int j, flag = 1; \n\
                for(j=2; j <= n/2; ++j) \n\
                { \n\
                    if (n%j == 0) \n\
                    { \n\
                        flag =0; \n\
                         break; \n\
                    } \n\
                 } \n\
            return flag;\n\
            }'
    tokens = [('int', 65), ('checkPrimeNumber', 82), ('int', 65), ('n', 82), ('int', 65), ('j', 82), (',', 34),
              ('flag', 82), ('1', 1), ('for', 62), ('j', 82), ('=', 7), ('2', 1), ('j', 82), ('n', 82), ('/', 5),
              ('2', 1), ('j', 82), ('if', 64), ('n', 82), ('%', 6), ('j', 82), ('0', 1), ('flag', 82), ('0', 1),
              ('break', 50), ('return', 68), ('flag', 82)]
    assert scan(in_c) == tokens