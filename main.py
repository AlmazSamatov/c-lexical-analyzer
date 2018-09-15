from lexical_analyzer import LexicalAnalyzer

f = open("in.c", "r")
lexical_analyzer = LexicalAnalyzer(f.read())
lexical_analyzer.scan()