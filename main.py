from urllib.request import urlopen
from bs4 import BeautifulSoup
from operator import eq
import urllib.request
from urllib import parse
import logging

def findFunction() :
    global num
    global flag
    titleBook = titleParsing[num].find('a').text
    print("%d." % (num+1))
    print("제목 : ", titleBook)
    location = locationParsing[num].find('a').text
    wh = 0 
    while location[wh]!="]":
        wh=wh+1
    print("위치 : ", end='')
    numList = list(range(0,wh+1))
    for j in numList:
        print(location[j], end = '')
    flag = 1
    detail = detailParsing[num].find('span').text
    if detail=="상세정보확인":
        print("\n대출가능")
    else:
        print("\n대출불가능")
    print("\n") 

def callFunction() :
    global num
    length = min(len(locationParsing), len(titleParsing))
    while num < length:
        findFunction()
        num = num+1
    if flag==0 :
        print("nothing has been found\n")

if __name__ == "__main__":
    logging.basicConfig(filename='example.log',level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')

    num=0
    flag=0
    title = input("책 제목을 입력해주세요 : ")
    html_tmpStart= "https://library.sogang.ac.kr/searchTotal/result?st=KWRD&si=TOTAL&q="
    html = urllib.parse.quote_plus(str(title))
    html_tmpEnd = "&x=0&y=0"
    FullURL = html_tmpStart + html + html_tmpEnd
    FullHTML = urllib.request.urlopen(FullURL)
    bsObject = BeautifulSoup(FullHTML, "html.parser")
    titleParsing = bsObject.findAll('p', attrs={'class':'listTitle'})
    locationParsing = bsObject.findAll('p', attrs={'class':'location'})
    detailParsing =  bsObject.findAll('p', attrs={'class':'location'})
    callFunction()