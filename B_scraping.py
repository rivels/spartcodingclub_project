import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.project



headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

##bugs spring

data = requests.get('https://music.bugs.co.kr/musicpd?tag_id=492',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

A_list=soup.select('#container > section > div > ul > li > figure > figcaption > a.title.hyrend')
B_spring_URL_list=[]

for i in A_list:
    B_spring_URL_list.append(i['href'])


for L in B_spring_URL_list:
    data = requests.get(L,headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    trs=soup.select('table > tbody > tr')
    B_spring_title = soup.select_one('#container > header > div > h1').text
    B_spring_image = soup.select_one('#basicInfoArea > div.thumbnails > a > div > span.album > img')['src']
    B_spring_tag1 = soup.select_one('#esAlbumTagArea > a:nth-child(3) > span').text
    B_spring_tag2 = soup.select_one('#esAlbumTagArea > a:nth-child(2) > span').text
    B_spring_num = (len(trs)-6)

    B_spring_doc={
        "title" : B_spring_title,
        "image" : B_spring_image,
        "tag_1" : B_spring_tag1,
        "tag_2" : B_spring_tag2,
        "num" : str(B_spring_num) + '곡'
    }
    db.bugs_spring.insert_one(B_spring_doc)

##bugs summer

#
data = requests.get('https://music.bugs.co.kr/musicpd?tag_id=254',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

A_list=soup.select('#container > section > div > ul > li > figure > figcaption > a.title.hyrend')
B_summer_URL_list=[]

for i in A_list:
    B_summer_URL_list.append(i['href'])


for L in B_summer_URL_list:
    data = requests.get(L,headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    trs=soup.select('table > tbody > tr')
    B_summer_title = soup.select_one('#container > header > div > h1').text
    B_summer_image = soup.select_one('#basicInfoArea > div.thumbnails > a > div > span.album > img')['src']
    B_summer_tag1 = soup.select_one('#esAlbumTagArea > a:nth-child(3) > span').text
    B_summer_tag2 = soup.select_one('#esAlbumTagArea > a:nth-child(2) > span').text
    B_summer_num = (len(trs)-6)

    B_summer_doc={
        "title" : B_summer_title,
        "image" : B_summer_image,
        "tag_1" : B_summer_tag1,
        "tag_2" : B_summer_tag2,
        "num" : str(B_summer_num) + '곡'
    }
    db.bugs_summer.insert_one(B_summer_doc)

#bugs_fall

data = requests.get('https://music.bugs.co.kr/musicpd?tag_id=781',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

A_list=soup.select('#container > section > div > ul > li > figure > figcaption > a.title.hyrend')
B_fall_URL_list=[]

for i in A_list:
    B_fall_URL_list.append(i['href'])


for L in B_fall_URL_list:
    data = requests.get(L,headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    trs=soup.select('table > tbody > tr')
    B_fall_title = soup.select_one('#container > header > div > h1').text
    B_fall_image = soup.select_one('#basicInfoArea > div.thumbnails > a > div > span.album > img')['src']
    B_fall_tag1 = soup.select_one('#esAlbumTagArea > a:nth-child(1) > span').text
    B_fall_tag2 = soup.select_one('#esAlbumTagArea > a:nth-child(2) > span').text
    B_fall_num = (len(trs)-6)

    B_fall_doc={
        "title" : B_fall_title,
        "image" : B_fall_image,
        "tag_1" : B_fall_tag1,
        "tag_2" : B_fall_tag2,
        "num" : str(B_fall_num) + '곡'
    }
    db.bugs_fall.insert_one(B_fall_doc)

#bugs_winter
data = requests.get('https://music.bugs.co.kr/musicpd?tag_id=1648',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

A_list=soup.select('#container > section > div > ul > li > figure > figcaption > a.title.hyrend')
B_winter_URL_list=[]

for i in A_list:
    B_winter_URL_list.append(i['href'])


for L in B_winter_URL_list:
    data = requests.get(L,headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    trs=soup.select('table > tbody > tr')
    B_winter_title = soup.select_one('#container > header > div > h1').text
    B_winter_image = soup.select_one('#basicInfoArea > div.thumbnails > a > div > span.album > img')['src']
    B_winter_tag1 = soup.select_one('#esAlbumTagArea > a:nth-child(1) > span').text
    B_winter_tag2 = soup.select_one('#esAlbumTagArea > a:nth-child(2) > span').text
    B_winter_num = (len(trs)-6)

    B_winter_doc={
        "title" : B_winter_title,
        "image" : B_winter_image,
        "tag_1" : B_winter_tag1,
        "tag_2" : B_winter_tag2,
        "num" : str(B_winter_num) + '곡'
    }
    db.bugs_winter.insert_one(B_winter_doc)