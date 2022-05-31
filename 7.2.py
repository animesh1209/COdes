fn=input("Enter file name:")
fh=open(fn)
count=0
x=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        a=line.find(":")
        b=line[a+1:]
        c=float(b)
        x=x+c
        count=count+1
print("count:",count)
print("sum:",x)
print("average:",(x/count))
