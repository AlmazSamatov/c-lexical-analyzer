from src.lexical_analyzer import scan
import src.preprocessor as preprocessor

print('Welcome to the C Lexical Analyzer! Before proceeding, make sure that you have put your code inside "in.c" file')
f = open("in.c", "r")
print(scan(preprocessor.start(f.read())))
