import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.project2

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'https://www.melon.com/dj/djfinder/djfinder_inform.htm?djSearchType=T&djSearchKeyword=%23%EB%85%B8%EB%9E%98%EB%B0%A9',
    headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

# djPlylstList > div > ul > li:nth-child(1) > div.thumb > a
Total = soup.select('#djPlylstList > div > ul > li')


base_url = 'https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq='
playlist_url = []
artist_list = []
playlist = []
doc ={}
i=1
for li in Total:
    S = li.select_one('div.thumb > a.image_typeAll')['href']
    playlist_url.append(base_url + (str(S)[65:74]))
print(playlist_url)

for url in playlist_url:
    data = requests.get(
        url,
        headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    # frm > div > table > tbody > tr:nth-child(1) > td:nth-child(5) > div > div > div.ellipsis.rank02 > a
    songs = soup.select('#frm > div > table > tbody > tr')
    playlist_name = (soup.select_one('#conts > div.section_info.d_djcol_list > div > div.entry > div.info > div.ellipsis.song_name').text)
    doc={'title' : playlist_name}
    for song in songs:
        artist = song.select_one('td:nth-child(5) > div > div > div.ellipsis.rank02 > a').text
        doc[i] = artist
        i+=1
    doc['title'] = doc['title'].replace('\n' , '').replace('\t' , '')
    db.playlist.insert_one(doc)
    print(doc)
    doc={}
    i=1
