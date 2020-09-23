import json
from pprint import pprint
file = open("data_of_task2.json","r+")
data = json.load(file)

# Decade_years = {1950 : [] , 1960 : [] , 1970 : [] , 1980 : [] , 1990 : [] , 2000 : [] , 2010 : [] , 2020 : []}
dict_ = {}
Decade = 1950
while Decade<=2020 :
    decade = str(Decade)
    list_ = []
    for year in data :    
        if decade[0:3] == year[0:3] :
            list_.append(data[year])        
    dict_[Decade] = list_
    Decade+=10
pprint(dict_)
file = open("data_of_task3.json","w")
data = json.dump( dict_ , file , indent = 4)

# pprint(dict_)          
# a=[]
# for i in data:
#     print(i)
#     b=int(i)%10
#     c=int(i)-b
#     a.append(c)
# print(list(set(a)))
    
    
    
    
    
    
    
    
    
    
    
    
    # for j in Decade_years :
    #     Decade_year2 = str(j)
    #     if Decade_year[0:3] == Decade_year2[0:3] :
    #         Decade_years[j].append(data[i])
# pprint(Decade_years)
# file = open("d.json", "w")
# file_data = json.dump(Decade_years , file , indent= 4)








# decade = []
# years = []
# dict_ = {}        
# for i in data :
#     year = str(i)
#     decade_ = []
#     if  i not in decade :
#         for j in data :
#             year_ = str(j)
#             if year[0:3] == year_[0:3] :
#                 decade.append(j)
#                 decade_.append(j)
#         x = 1950 
#         while True :
#             dict_[i] =         







import json
import requests 
from bs4 import BeautifulSoup 
url = "https://www.imdb.com/title/tt0066763/"
response = requests.get(url)
Soup = BeautifulSoup(response.text , "html.parser")
div = Soup.find('div' , class_ = 'title_wrapper').h1.get_text()
movie_name = ''
for i in div :
    if i != '(' :
        movie_name+=i
    else:
        break        
Duration = []        
sub_text = Soup.find('div', class_='subtext')
time = sub_text.find('time').text.strip()
list_ = list(time)
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
time_of_movie = str(time_of_movie)
time_of_movie += ' mins'
gener = sub_text.find_all('a')
list_of_gener = []
for i in gener :
    list_of_gener.append(i.text)
list_of_gener.pop()
summary = ''            
div_ = Soup.find('div' , class_ = 'plot_summary')
bio = div_.find('div' , class_ = 'summary_text')
summary += bio.text.strip()
summary_item = div_.find('div' , class_ = 'credit_summary_item')
h4 