import re

name = raw_input("Enter file:")
if len(name) < 1: name = "regex_sum_42.txt"
handle = open(name)
sum=0
text = handle.read()
lst = re.findall('[0-9]+',text)
print lst

for x in lst:
    val=int(x)
    sum=sum+val

print sum

