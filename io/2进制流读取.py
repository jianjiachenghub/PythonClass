fo = open("lex.txt", "rb")
lines = fo.read().decode('utf-8').split('\r\n')
print(lines)