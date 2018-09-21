from lexical_analyzer import scan

f = open("in.c", "r")
print(scan(f.read()))
