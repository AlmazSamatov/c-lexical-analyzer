from lexical_analyzer import scan

f = open("in.c", "r")
lexical_analyzer = scan(f.read())
lexical_analyzer.scan()