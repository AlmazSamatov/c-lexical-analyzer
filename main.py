from lexical_analyzer import scan
import preprocessor

f = open("in.c", "r")
print(preprocessor.start(f.read()))
