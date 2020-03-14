from urllib.request import urlopen
from bs4 import BeautifulSoup
from operator import eq
import urllib.request
from urllib import parse
import logging

'''
    3/14 from 상빈
    전역 변수를 사용하지 않을 수는 없을까? (전역변수는 값이 생각지도 않게 변할 수 있어서 위험)

'''
def findFunction() :
    global bookIndex
    global searchFlag
    titleBook = titleParsing[bookIndex].find('a').text
    print("%d." % (bookIndex+1))
    print("제목 : ", titleBook)
    location = locationParsing[bookIndex].find('a').text

    split = location.find(']')
    print("위치 : ", end='')
    for j in range(0,split+1):
        print(location[j], end = '')

    searchFlag = 1
    detail = detailParsing[bookIndex].find('span').text
    if detail=="상세정보확인":
        print("\n대출가능")
    else:
        print("\n대출불가능")
    print("\n") 

def callFunction() :
    global bookIndex
    numOfBooks = min(len(locationParsing), len(titleParsing))
    while bookIndex < numOfBooks:
        findFunction()
        bookIndex = bookIndex + 1

    logging.debug('%d book has been searched' % bookIndex)    

    if searchFlag==0 :
        print("nothing has been found\n")

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='example.log',level=logging.DEBUG)
    logging.debug('--------------------------')
    logging.debug('program starts')

    bookIndex = 0
    searchFlag=0
    title = input("책 제목을 입력해주세요 : ")
    StartURL= "https://library.sogang.ac.kr/searchTotal/result?st=KWRD&si=TOTAL&q="
    titleURL = urllib.parse.quote_plus(str(title))
    endURL = "&x=0&y=0"
    FullURL = StartURL + titleURL + endURL
    FullHTML = urllib.request.urlopen(FullURL)
    bsObject = BeautifulSoup(FullHTML, "html.parser")
    titleParsing = bsObject.findAll('p', attrs={'class':'listTitle'})
    logging.debug('Title has been parsed')

    locationParsing = bsObject.findAll('p', attrs={'class':'location'})
    logging.debug('Location & availability has been parsed')
    detailParsing = locationParsing.copy()

    callFunction()

    logging.debug('program ends')
