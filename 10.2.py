name=input("Enter file:")
handle=open(name)
count=dict()
for line in handle:
    if line.startswith('From '):
        words=line.split()
        word=words[5]
        wrd=word.split(':')
        ans=wrd[0]
        count[ans]=count.get(ans,0)+1
for k,v in sorted(count.items()):
    print(k,v)
