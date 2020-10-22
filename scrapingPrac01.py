import requests
from bs4 import BeautifulSoup


#melon 봄
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data_Mspring = requests.get('https://www.melon.com/dj/djfinder/djfinder_inform.htm?djSearchType=T&djSearchKeyword=%EB%B4%84',headers=headers)
soup_Mspring = BeautifulSoup(data_Mspring.text, 'html.parser')

melon_playlist_spring=[]

Mlist1=soup_Mspring.select('#djPlylstList > div > ul > li > div.entry > div.info')

for i in Mlist1:
    M_playlist1_title = i.select_one('a.ellipsis.album_name').text
    M_playlist1_link = i.select_one('a.ellipsis.album_name')['href']
    melon_playlist_spring.append(M_playlist1_title.strip())
    melon_playlist_spring.append((M_playlist1_link))

print(melon_playlist_spring)
#melon 여름

#
# data_Msummer = requests.get('https://www.melon.com/dj/djfinder/djfinder_inform.htm?djSearchType=T&djSearchKeyword=%ED%95%B4%EB%B3%80',headers=headers)
# soup_Msummer = BeautifulSoup(data_Msummer.text, 'html.parser')
#
# melon_playlist_summer=[]
#
# Mlist2=soup_Msummer.select('#djPlylstList > div > ul > li > div.entry > div.info')
#
# for j in Mlist2:
#     M_playlist2 = j.select_one('a.ellipsis.album_name').text
#     melon_playlist_summer.append(M_playlist2.strip())
# print(melon_playlist_summer)
#
# #melon 가을
# data_Mfall = requests.get('https://www.melon.com/dj/djfinder/djfinder_inform.htm?djSearchType=T&djSearchKeyword=%23%EA%B0%80%EC%9D%84',headers=headers)
# soup_Mfall = BeautifulSoup(data_Mfall.text, 'html.parser')
#
# melon_playlist_fall=[]
#
# Mlist3=soup_Mfall.select('#djPlylstList > div > ul > li > div.entry > div.info')
#
# for k in Mlist3:
#     M_playlist3 = k.select_one('a.ellipsis.album_name').text
#     melon_playlist_fall.append(M_playlist3.strip())
# print(melon_playlist_fall)
#
# #melon 겨울
# data_Mwinter = requests.get('https://www.melon.com/dj/djfinder/djfinder_inform.htm?djSearchType=T&djSearchKeyword=%23%EA%B2%A8%EC%9A%B8',headers=headers)
# soup_Mwinter = BeautifulSoup(data_Mwinter.text, 'html.parser')
#
# melon_playlist_winter=[]
#
# Mlist4=soup_Mwinter.select('#djPlylstList > div > ul > li > div.entry > div.info')
#
# for k in Mlist4:
#     M_playlist4 = k.select_one('a.ellipsis.album_name').text
#     melon_playlist_winter.append(M_playlist4.strip())
# print(melon_playlist_winter)