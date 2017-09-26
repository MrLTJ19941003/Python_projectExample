from datetime import datetime
import re,urllib.request
now=datetime.now()
print(now.day)
print(datetime.today())

day='Wed, 27 May 2015 11:00 am CST'
print(re.split(r'[\s\,]+',day) )

from bs4 import BeautifulSoup

doc = urllib.request.urlopen('http://www.baidu.com')
soup = BeautifulSoup(doc)

print(soup.prettify())
head = soup.contents[0].contents[0]

print(head.parent.name)