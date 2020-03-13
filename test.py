from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request
from urllib import parse

title = input("책 제목을 입력해주세요 : ")

html_tmpStart= "https://library.sogang.ac.kr/searchTotal/result?st=KWRD&si=TOTAL&q="
html = urllib.parse.quote_plus(str(title))
html_tmpEnd = "&x=0&y=0"
FullURL = html_tmpStart + html + html_tmpEnd
FullHTML = urllib.request.urlopen(FullURL)
bsObject = BeautifulSoup(FullHTML, "html.parser")

#print(bsObject)
parsing = bsObject.findAll('p', attrs={'class':'location'})
print(type(parsing))

i = 0
while i < len(parsing):
    location = parsing[i].find('a').text
    print(location)
    i += 1