import requests
from bs4 import BeautifulSoup


#melon 봄
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data_Mspring = requests.get('https://www.melon.com/dj/djfinder/djfinder_inform.htm?djSearchType=T&djSearchKeyword=%EB%B4%84',headers=headers)
soup_Mspring = BeautifulSoup(data_Mspring.text, 'html.parser')

#멜론 봄 플레이리스트 이름&이미지가 들어갈 리스트 정의 추후 딕셔너리형태로 바꿔야 될 수도 있을
Mspring_title=Mspring_img=[]

'''
for문이 크롤링 하나당 하나씩 생기는게 아니라,
하나의 for문에 여러가지 항목(제목,이미지,곡수,좋아요수)을 크롤링할 수 있도록,또 동시
계절별 db에 dictionary 형식으로
{
 'melon_spring_title':M_playlist1.strip()
 'melon_spring_img':M_playlist11
 .....
} 와 같은 형식으로 입력해야할듯

플레이리스트 제목, DJ, 태그, 이미지
'''

Mlist_spring_title=soup_Mspring.select('#djPlylstList > div > ul > li > div.entry > div.info')
Mlist_spring_img=soup_Mspring.select('#djPlylstList > div > ul > li > div.thumb > a')
for title in Mlist_spring_title:
    M_playlist1=title.select_one('a.ellipsis.album_name').text
    Mspring_title.append(M_playlist1.strip())
for img in Mlist_spring_img:
    M_playlist11=img.select_one('img')['src']
    Mspring_img.append(M_playlist11)
print(Mspring_title,Mspring_img)
#melon 여름


data_Msummer = requests.get('https://www.melon.com/dj/djfinder/djfinder_inform.htm?djSearchType=T&djSearchKeyword=%ED%95%B4%EB%B3%80',headers=headers)
soup_Msummer = BeautifulSoup(data_Msummer.text, 'html.parser')

melon_playlist_summer=[]

Msummer_title=soup_Msummer.select('#djPlylstList > div > ul > li > div.entry > div.info')

for summertitle in Msummer_title:
    M_playlist2 = summertitle.select_one('a.ellipsis.album_name').text
    melon_playlist_summer.append(M_playlist2.strip())
print(melon_playlist_summer)

#melon 가을
data_Mfall = requests.get('https://www.melon.com/dj/djfinder/djfinder_inform.htm?djSearchType=T&djSearchKeyword=%23%EA%B0%80%EC%9D%84',headers=headers)
soup_Mfall = BeautifulSoup(data_Mfall.text, 'html.parser')

melon_playlist_fall=[]

Mlist_fall_title=soup_Mfall.select('#djPlylstList > div > ul > li > div.entry > div.info')

for k in Mlist_fall_title:
    M_playlist3 = k.select_one('a.ellipsis.album_name').text
    melon_playlist_fall.append(M_playlist3.strip())
print(melon_playlist_fall)

#melon 겨울
data_Mwinter = requests.get('https://www.melon.com/dj/djfinder/djfinder_inform.htm?djSearchType=T&djSearchKeyword=%23%EA%B2%A8%EC%9A%B8',headers=headers)
soup_Mwinter = BeautifulSoup(data_Mwinter.text, 'html.parser')

melon_playlist_winter=[]

Mlist_winter_title=soup_Mwinter.select('#djPlylstList > div > ul > li > div.entry > div.info')

for l in Mlist_winter_title:
    M_playlist4 = l.select_one('a.ellipsis.album_name').text
    melon_playlist_winter.append(M_playlist4.strip())
print(melon_playlist_winter)