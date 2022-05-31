fname = input("Enter file name: ")
fh = open(fname)
b = list()
for line in fh:
    line=line.rstrip()
    a=line.split()
    for pieces in a:
        if pieces not in b:
            b.append(pieces)
b.sort()
print(b)
