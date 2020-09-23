import json,os,requests
from bs4 import BeautifulSoup
from pprint import pprint
import time
file = open('deepak.json', 'r')
data = json.load(file)
Counter = 0
details_of_movie = []
c = 0
for i in data :
    c+=1
    url = i['Url']
    # UrL = url[27:36]
    
    # if os.path.exists(UrL) :
    #     print("Exists")
    #     print(c)
    
    # else:
    time.sleep(3)   
    response = requests.get(url)
    Soup = BeautifulSoup(response.text , "html.parser")
    Movies = {}
    div = Soup.find('div' , class_ = 'title_wrapper').h1.get_text()
    movie_name = ''
    Movie_details = []
    for i in div :
        if i != '\xa0' :
            movie_name+=i
        else:
            break

    Movies['Name'] = movie_name



    sub_text = Soup.find('div', class_='subtext')
    timeS = sub_text.find('time').text.strip()
    list_ = list(timeS)
    Duration = ''
    for i in list_ :
        if i != "h" :
            Duration+=i
        else:
            break    
    Duration = int(Duration)
    time_ = Duration*60
    a = time_
    b = ''
    for i in range(len(list_)):
        index_ = i - len(list_)
        if list_[index_] in "0123456789" :
            b+=list_[index_]
        elif list_[index_] == "h" :
            break
    time_of_movie = a+int(b)

    Movies['Runtime'] = time_of_movie




    gener = sub_text.find_all('a')
    list_of_gener = []
    for i in gener :
        list_of_gener.append(i.text)
    list_of_gener.pop()

    Movies['Genre'] = list_of_gener





    summary = ''            
    div_ = Soup.find('div' , class_ = 'plot_summary')
    bio = div_.find('div' , class_ = 'summary_text')
    summary += bio.text.strip()

    Movies['summary'] = summary






    credit_summary_item = div_.find_all('div' , class_ = 'credit_summary_item')
    Directors = []
    for i in credit_summary_item :
        if "Director" in i.text :
            Director = i.find_all('a')
            for j in Director :
                Directors.append(j.text)

    Movies['Director'] = Directors






    div__ = Soup.find('div' , class_ = 'poster')
    Poster = div__.find('a')
    images= Poster.find("img")['src']

    Movies['Image'] = images





    div1_ = Soup.find_all('div' , class_ = 'txt-block')
    languages = []
    for i in div1_:
        if "Country" in i.text :
            Country= i.find("a").text

    Movies['Country'] = Country
    for i in div1_  :
        if "Language" in i.text :
            Language = i.find_all("a")
            for j in Language :
                languages.append(j.text)   

    Movies['Languages'] = languages
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
    Movies['cast'] = cast_            
    details_of_movie.append(Movies)
    Counter+=1
    pprint(Movies)
    print(c)
file = open('Data_13.json', 'w')
data = json.dump(details_of_movie , file , indent = 4)
    
