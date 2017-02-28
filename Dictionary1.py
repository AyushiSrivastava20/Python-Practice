fname = raw_input("Enter file name: ")
fh = open(fname)
text= fh.read()
words=text.split()

counts=dict()

for word in words:
    counts[word]=counts.get(word,0)+1

print counts.items()

bigcount=None
bigword=None

for word,count in counts.items():
    if bigcount is None or count>bigcount:
       bigword=word
       bigcount=count

print 'bigword', bigword

print 'bigcount', bigcount