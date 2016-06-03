# Upisi u fajl
with open("test.txt", "wt") as out_file:
    out_file.write("This Text is going to out file\nLook at it and see!")
 
# Procitaj iz fajla
with open("test.txt", "rt") as in_file:
    text = in_file.read()
 
print(text)
