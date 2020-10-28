import requests
from bs4 import BeautifulSoup


#melon 봄
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data_Mspring = requests.get('https://www.melon.com/dj/djfinder/djfinder_inform.htm?djSearchType=T&djSearchKeyword=%EB%B4%84',headers=headers)
soup_Mspring = BeautifulSoup(data_Mspring.text, 'html.parser')

A=[]
Mlist_spring_num=soup_Mspring.select('#djPlylstList > div > ul > li > div.entry > div.meta > span')

Total=soup_Mspring.select('#djPlylstList > div > ul > li > div.entry')

for _ in Total:
    num=_.select_one('div.meta > span')
    A.append(num.text)
print(A)
