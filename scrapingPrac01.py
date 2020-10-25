import requests
from bs4 import BeautifulSoup


#melon 봄
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data_Mspring = requests.get('https://www.melon.com/dj/djfinder/djfinder_inform.htm?djSearchType=T&djSearchKeyword=%EB%B4%84',headers=headers)
soup_Mspring = BeautifulSoup(data_Mspring.text, 'html.parser')

#djPlylstList > div > ul > li:nth-child(1) // 멜론 플레이리스트 li 까지의 selector
Mlist=soup_Mspring.select('#djPlylstList > div > ul > li')
# print(Mlist)

#djPlylstList > div > ul > li:nth-child(1) > div.entry > div.info > a.ellipsis.album_name // 플레이리스트 title
#djPlylstList > div > ul > li:nth-child(1) > div.entry > div.info > a.ellipsis.artist_name // DJ명도 동일하게 안됨..
#djPlylstList > div > ul > li:nth-child(1) > div.entry > div.tag_list > a:nth-child(1) > span

for M in Mlist:
    M_tag=M.select_one('div.entry > div.tag_list > a > span').text
    print(M_tag)