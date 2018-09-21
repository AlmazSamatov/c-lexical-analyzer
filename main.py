import preprocessor

f = open("in.c", "r")
c_code = f.read()
preprocessor.start(c_code)