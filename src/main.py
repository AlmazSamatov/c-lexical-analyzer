from src.lexical_analyzer import get_next_token, scan
import src.preprocessor as preprocessor

input('Welcome to the C Lexical Analyzer! Before proceeding, make sure that you have put your code inside "in.c" file\n'
      'Press Enter to continue...')
with open("in.c", "r") as file:
    try:
        preprocessed_code = preprocessor.start(file.read())

        while True:
            token = get_next_token(preprocessed_code)
            input('Press Enter to print next token')
            print(token)
            if token[0] == '_EOF':
                break

    except FileNotFoundError as e:
        print('Error! File in #include statement with name: {} not found.'.format(e.filename))
        exit(0)
    except BaseException as e:
        print('Error! Unable to correctly preprocess #include statement. Error in : ' + e.args[0])
        exit(0)


