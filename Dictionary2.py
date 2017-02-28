name = raw_input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    if line.startswith('From'):
        words = line.split()
        value = words[1]
        counts[value] = counts.get(value, 0) + 1

bigcount = None
bigword = None

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print bigword, bigcount

