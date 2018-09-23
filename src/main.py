from src.lexical_analyzer import get_next_token, scan
import src.preprocessor as preprocessor

f = open("in.txt", "r")
preprocessed_code = preprocessor.start(f.read())
f = open("out.txt", 'w')
while True:
    token = get_next_token(preprocessed_code)
    f.write(str(token)+"\n")
    if token[0] == '_EOF':
        break
