fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
  words= line.rstrip().split()
  print words
  for w in words:
     if not w in lst:
        lst.append(w)

lst.sort()
print lst
