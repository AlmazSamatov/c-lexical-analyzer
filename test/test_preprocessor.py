from src.preprocessor import *


def test_replace_all():
    input_string = '#define DVA 2\n' \
                   '// user-defined function to check prime number \n\
                int checkPrimeNumber(int n) \n\
                { \n\
                    int j, flag = 1; \n\
                    for(j=DVA; j <= n/DVA; ++j) \n\
                    { \n\
                        if (n%j == 0) \n\
                        { \n\
                            flag =0; \n\
                             break; \n\
                        } \n\
                     } \n\
                return flag;\n\
                }'
    valid_string = '\n// user-defined function to check prime number \n\
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
    assert replace_all(input_string, 'DVA', '2') == valid_string


def scan_for_define():
    input_string = '#define DVA 2\n' \
                   '// user-defined function to check prime number \n\
                int checkPrimeNumber(int n) \n\
                { \n\
                    int j, flag = 1; \n\
                    for(j=DVA; j <= n/DVA; ++j) \n\
                    { \n\
                        if (n%j == 0) \n\
                        { \n\
                            flag =0; \n\
                             break; \n\
                        } \n\
                    } \n\
                return flag;\n\
                }'
    result = {
        'DVA': '2'
    }
    assert scan_for_define(input_string) == result


def test_start():
    input_string = '#define DVA 2\n' \
                   '// user-defined function to check prime number \n\
                int checkPrimeNumber(int n) \n\
                { \n\
                    int j, flag = 1; \n\
                    for(j=DVA; j <= n/DVA; ++j) \n\
                    { \n\
                        if (n%j == 0) \n\
                        { \n\
                            flag =0; \n\
                            break; \n\
                        } \n\
                    } \n\
                return flag;\n\
                }'
    valid_string = '\n// user-defined function to check prime number \n\
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
    assert start(input_string) == valid_string
