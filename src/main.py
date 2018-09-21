from src.lexical_analyzer import scan, find_type_of_lexeme
from src.util import *
from src.preprocessor_tool import PreprocessorTool

input_string = '// user-defined function to check prime number \n\
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
tool = PreprocessorTool(input_string)
tool.replace_all('DVA', '2')
