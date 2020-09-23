import requests,os,json
from bs4 import BeautifulSoup
from pprint import pprint
import time
file = open('deepak.json','r')
data = json.load(file)
list_ = []
c = 0
for n in data :
    c+=1
    Url = n['Url']
    time.sleep(3)
    response = requests.get(Url)
    Soup = BeautifulSoup(response.text , 'html.parser')
    cast_list = Soup.find('table' , class_ = 'cast_list') 
    trs = cast_list.find_all('tr')
    cast_ = []
    for i in trs :
        td = i.find_all('td',class_=False)
        for j in td:
            cast = {}
            a = j.find_all('a')
            if a:
                Link = a[0]['href']
                cast['imdb_id'] = Link[6:15]
                cast['Name'] = a[0].text.strip()
                cast_.append(cast)
    list_.append(cast_)
    pprint(cast_)
    print(c)                    
file = open('cast.json','w')
data = json.dump(list_, file , indent = 4)
