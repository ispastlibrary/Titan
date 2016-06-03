import glob, os
os.chdir("/home/polaznik/AST2/David/rmob")
a = []
b = []
for file in glob.glob("*"):
    a.append(file)
m = open('coussens_032015rmob.TXT', 'r')
z = m.readline()
print(z)
