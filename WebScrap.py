import urllib

from BeautifulSoup import *

count=0
sum=0


url= raw_input('Enter url')
html=urllib.urlopen(url).read()
soup=BeautifulSoup(html)

tags1 = soup('a')

for tag1 in tags1:
    print tag1.get('href', None)


tags = soup('span')

for tag in tags:
    count=count+1
    sum=sum+int(tag.text)

print count
print sum