import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.project


#melon 봄
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data_Mspring = requests.get('https://www.melon.com/dj/djfinder/djfinder_inform.htm?djSearchType=T&djSearchKeyword=%EB%B4%84',headers=headers)
soup_Mspring = BeautifulSoup(data_Mspring.text, 'html.parser')

Mspring_title=[]
Mspring_img=[]
Mspring_tag=[]
Mspring_num=[]

Mlist_spring_title=soup_Mspring.select('#djPlylstList > div > ul > li > div.entry > div.info')
Mlist_spring_img=soup_Mspring.select('#djPlylstList > div > ul > li > div.thumb > a')
Mlist_spring_tag=soup_Mspring.select('#djPlylstList > div > ul > li > div.entry > div.tag_list > a.tag_item')
Mlist_spring_num=soup_Mspring.select('#djPlylstList > div > ul > li > div.entry > div.meta > span')
for title in Mlist_spring_title:
    M_playlist1=title.select_one('a.ellipsis.album_name').text
    Mspring_title.append(M_playlist1.strip())
for img in Mlist_spring_img:
    M_playlist11=img.select_one('img')['src']
    Mspring_img.append(M_playlist11)
for tag in Mlist_spring_tag:
    Mspring_tag.append(tag.text)
for num in Mlist_spring_num:
    Mspring_num.append(num.text)
for d in range(0,len(Mlist_spring_title)):
    M_sprint_doc ={
        'title' : Mspring_title[d],
        'img' : Mspring_img[d],
        'tag_1' : Mspring_tag[d],
        'tag_2' : Mspring_tag[d+1],
        'num' : Mspring_num[d]
    }
    db.melon_spring.insert_one(M_sprint_doc)


#melon 여름

data_Msummer = requests.get('https://www.melon.com/dj/djfinder/djfinder_inform.htm?djSearchType=T&djSearchKeyword=%ED%95%B4%EB%B3%80',headers=headers)
soup_Msummer = BeautifulSoup(data_Msummer.text, 'html.parser')

Msummer_title=[]
Msummer_img=[]
Msummer_tag=[]
Msummer_num=[]

Mlist_summer_title=soup_Msummer.select('#djPlylstList > div > ul > li > div.entry > div.info')
Mlist_summer_img=soup_Msummer.select('#djPlylstList > div > ul > li > div.thumb > a')
Mlist_summer_tag=soup_Msummer.select('#djPlylstList > div > ul > li > div.entry > div.tag_list > a.tag_item')
Mlist_summer_num=soup_Msummer.select('#djPlylstList > div > ul > li > div.entry > div.meta > span')
for title in Mlist_summer_title:
    M_playlist1=title.select_one('a.ellipsis.album_name').text
    Msummer_title.append(M_playlist1.strip())
for img in Mlist_summer_img:
    M_playlist11=img.select_one('img')['src']
    Msummer_img.append(M_playlist11)
for tag in Mlist_summer_tag:
    Msummer_tag.append(tag.text)
for num in Mlist_summer_num:
    Msummer_num.append(num.text)
for d in range(0,len(Mlist_summer_title)):
    M_summer_doc ={
        'title' : Msummer_title[d],
        'img' : Msummer_img[d],
        'tag_1' : Msummer_tag[d],
        'tag_2' : Msummer_tag[d+1],
        'num' : Msummer_num[d]
    }
    db.melon_summer.insert_one(M_summer_doc)


#melon 가을

data_Mfall = requests.get('https://www.melon.com/dj/djfinder/djfinder_inform.htm?djSearchType=T&djSearchKeyword=%23%EA%B0%80%EC%9D%84',headers=headers)
soup_Mfall = BeautifulSoup(data_Mfall.text, 'html.parser')

Mfall_title=[]
Mfall_img=[]
Mfall_tag=[]
Mfall_num=[]

Mlist_fall_title=soup_Mfall.select('#djPlylstList > div > ul > li > div.entry > div.info')
Mlist_fall_img=soup_Mfall.select('#djPlylstList > div > ul > li > div.thumb > a')
Mlist_fall_tag=soup_Mfall.select('#djPlylstList > div > ul > li > div.entry > div.tag_list > a.tag_item')
Mlist_fall_num=soup_Mfall.select('#djPlylstList > div > ul > li > div.entry > div.meta > span')
for title in Mlist_fall_title:
    M_playlist1=title.select_one('a.ellipsis.album_name').text
    Mfall_title.append(M_playlist1.strip())
for img in Mlist_fall_img:
    M_playlist11=img.select_one('img')['src']
    Mfall_img.append(M_playlist11)
for tag in Mlist_fall_tag:
    Mfall_tag.append(tag.text)
for num in Mlist_fall_num:
    Mfall_num.append(num.text)
for d in range(0,len(Mlist_fall_title)):
    M_fall_doc ={
        'title' : Mfall_title[d],
        'img' : Mfall_img[d],
        'tag_1' : Mfall_tag[d],
        'tag_2' : Mfall_tag[d+1],
        'num' : Mfall_num[d]
    }
    db.melon_fall.insert_one(M_fall_doc)


#melon 겨울

data_Mwinter = requests.get('https://www.melon.com/dj/djfinder/djfinder_inform.htm?djSearchType=T&djSearchKeyword=%23%EA%B2%A8%EC%9A%B8',headers=headers)
soup_Mwinter = BeautifulSoup(data_Mwinter.text, 'html.parser')

Mwinter_title=[]
Mwinter_img=[]
Mwinter_tag=[]
Mwinter_num=[]

Mlist_winter_title=soup_Mwinter.select('#djPlylstList > div > ul > li > div.entry > div.info')
Mlist_winter_img=soup_Mwinter.select('#djPlylstList > div > ul > li > div.thumb > a')
Mlist_winter_tag=soup_Mwinter.select('#djPlylstList > div > ul > li > div.entry > div.tag_list > a.tag_item')
Mlist_winter_num=soup_Mwinter.select('#djPlylstList > div > ul > li > div.entry > div.meta > span')
for title in Mlist_winter_title:
    M_playlist1=title.select_one('a.ellipsis.album_name').text
    Mwinter_title.append(M_playlist1.strip())
for img in Mlist_winter_img:
    M_playlist11=img.select_one('img')['src']
    Mwinter_img.append(M_playlist11)
for tag in Mlist_winter_tag:
    Mwinter_tag.append(tag.text)
for num in Mlist_winter_num:
    Mwinter_num.append(num.text)
for d in range(0,len(Mlist_winter_title)):
    M_winter_doc ={
        'title' : Mwinter_title[d],
        'img' : Mwinter_img[d],
        'tag_1' : Mwinter_tag[d],
        'tag_2' : Mwinter_tag[d+1],
        'num' : Mwinter_num[d]
    }
    db.melon_winter.insert_one(M_winter_doc)



#genie spring

data = requests.get('https://www.genie.co.kr/playlist/tags?tags=ST0025%7C%7C%EB%B4%84',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

#showTagList > div.recom-wrap > ul > li > div.item_info > div.tag > a:nth-child(7)  // 태그는 6,7번
#showTagList > div.recom-wrap > ul > li > div.item_info > div.title > a')  //  플레이리스트 이름
#showTagList > div.recom-wrap > ul > li:nth-child(1) > div.item_info > ul > li.num
Gspring_title=[]
Gspring_image=[]
Gspring_tag=[]
Gspring_num=[]

Total = soup.select('#showTagList > div.recom-wrap > ul > li')

for i in Total:
    Gspring_image.append(i.select_one('div.item_cover > a.cover > img')['src'])
    Gspring_title.append(i.select_one('div.item_info > div.title > a').text)
    Gspring_tag.append(i.select_one('div.item_info > div.tag > a:nth-child(6)').text)
    Gspring_tag.append(i.select_one('div.item_info > div.tag > a:nth-child(7)').text)
    Gspring_num.append(i.select_one('div.item_info > ul > li.num').text)
    Gspring_doc ={
        "title" : i.select_one('div.item_info > div.title > a').text,
        "image" : i.select_one('div.item_cover > a.cover > img')['src'],
        "tag_1" : i.select_one('div.item_info > div.tag > a:nth-child(6)').text,
        "tag_2" : i.select_one('div.item_info > div.tag > a:nth-child(7)').text,
        "num" : i.select_one('div.item_info > ul > li.num').text
    }
    db.genie_spring.insert_one(Gspring_doc)

#genie_summer

data = requests.get('https://www.genie.co.kr/playlist/tags?tags=ST0028%7C%7C%EC%97%AC%EB%A6%84',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

#showTagList > div.recom-wrap > ul > li > div.item_info > div.tag > a:nth-child(7)  // 태그는 6,7번
#showTagList > div.recom-wrap > ul > li > div.item_info > div.title > a')  //  플레이리스트 이름
#showTagList > div.recom-wrap > ul > li:nth-child(1) > div.item_info > ul > li.num
Gsummer_title=[]
Gsummer_image=[]
Gsummer_tag=[]
Gsummer_num=[]

Total = soup.select('#showTagList > div.recom-wrap > ul > li')

for i in Total:
    Gsummer_image.append(i.select_one('div.item_cover > a.cover > img')['src'])
    Gsummer_title.append(i.select_one('div.item_info > div.title > a').text)
    Gsummer_tag.append(i.select_one('div.item_info > div.tag > a:nth-child(6)').text)
    Gsummer_tag.append(i.select_one('div.item_info > div.tag > a:nth-child(5)').text)
    Gsummer_num.append(i.select_one('div.item_info > ul > li.num').text)
    Gsummer_doc ={
        "title" : i.select_one('div.item_info > div.title > a').text,
        "image" : i.select_one('div.item_cover > a.cover > img')['src'],
        "tag_1" : i.select_one('div.item_info > div.tag > a:nth-child(6)').text,
        "tag_2" : i.select_one('div.item_info > div.tag > a:nth-child(5)').text,
        "num" : i.select_one('div.item_info > ul > li.num').text
    }
    db.genie_summer.insert_one(Gsummer_doc)

#genie_fall

data = requests.get('https://www.genie.co.kr/playlist/tags?tags=ST0015%7C%7C%EA%B0%80%EC%9D%84',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

#showTagList > div.recom-wrap > ul > li > div.item_info > div.tag > a:nth-child(7)  // 태그는 6,7번
#showTagList > div.recom-wrap > ul > li > div.item_info > div.title > a')  //  플레이리스트 이름
#showTagList > div.recom-wrap > ul > li:nth-child(1) > div.item_info > ul > li.num
Gfall_title=[]
Gfall_image=[]
Gfall_tag=[]
Gfall_num=[]

Total = soup.select('#showTagList > div.recom-wrap > ul > li')

for i in Total:
    Gfall_image.append(i.select_one('div.item_cover > a.cover > img')['src'])
    Gfall_title.append(i.select_one('div.item_info > div.title > a').text)
    Gfall_tag.append(i.select_one('div.item_info > div.tag > a:nth-child(6)').text)
    Gfall_tag.append(i.select_one('div.item_info > div.tag > a:nth-child(5)').text)
    Gfall_num.append(i.select_one('div.item_info > ul > li.num').text)
    Gfall_doc ={
        "title" : i.select_one('div.item_info > div.title > a').text,
        "image" : i.select_one('div.item_cover > a.cover > img')['src'],
        "tag_1" : i.select_one('div.item_info > div.tag > a:nth-child(6)').text,
        "tag_2" : i.select_one('div.item_info > div.tag > a:nth-child(5)').text,
        "num" : i.select_one('div.item_info > ul > li.num').text
    }
    db.genie_fall.insert_one(Gfall_doc)

#genie_winter
data = requests.get('https://www.genie.co.kr/playlist/tags?tags=ST0016%7C%7C%EA%B2%A8%EC%9A%B8',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

#showTagList > div.recom-wrap > ul > li > div.item_info > div.tag > a:nth-child(7)  // 태그는 6,7번
#showTagList > div.recom-wrap > ul > li > div.item_info > div.title > a')  //  플레이리스트 이름
#showTagList > div.recom-wrap > ul > li:nth-child(1) > div.item_info > ul > li.num
Gwinter_title=[]
Gwinter_image=[]
Gwinter_tag=[]
Gwinter_num=[]

Total = soup.select('#showTagList > div.recom-wrap > ul > li')

for i in Total:
    Gwinter_image.append(i.select_one('div.item_cover > a.cover > img')['src'])
    Gwinter_title.append(i.select_one('div.item_info > div.title > a').text)
    Gwinter_tag.append(i.select_one('div.item_info > div.tag > a:nth-child(6)').text)
    Gwinter_tag.append(i.select_one('div.item_info > div.tag > a:nth-child(5)').text)
    Gwinter_num.append(i.select_one('div.item_info > ul > li.num').text)
    Gwinter_doc ={
        "title" : i.select_one('div.item_info > div.title > a').text,
        "image" : i.select_one('div.item_cover > a.cover > img')['src'],
        "tag_1" : i.select_one('div.item_info > div.tag > a:nth-child(6)').text,
        "tag_2" : i.select_one('div.item_info > div.tag > a:nth-child(5)').text,
        "num" : i.select_one('div.item_info > ul > li.num').text
    }
    db.genie_winter.insert_one(Gwinter_doc)