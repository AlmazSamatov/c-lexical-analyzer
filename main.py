from lexical_analyzer import Lexical_Analyzer

f = open("in.c", "r")
lexical_analyzer = Lexical_Analyzer(f.read())
lexical_analyzer.scan()