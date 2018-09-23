from src.lexical_analyzer import get_next_token, scan
import src.preprocessor as preprocessor

input('Welcome to the C Lexical Analyzer! Before proceeding, make sure that you have put your code inside "in.c" file\n'
      'Press Enter to continue...')
f = open("../in.c", "r")
preprocessed_code = preprocessor.start(f.read())
print(scan(preprocessed_code))
while True:
    token = get_next_token(preprocessed_code)
    input('Press Enter to print next token')
    print(token)
    if token[0] == '_EOF':
        break
