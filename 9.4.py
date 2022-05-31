name=input("Enter file name:")
hand=open(name)
counts=dict()
for line in hand:
    if line.startswith('From '):
        words=line.split()
        word=words[1]
        counts[word]=counts.get(word,0)+1
bigword=None
bigcount=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
print(bigword,bigcount)
