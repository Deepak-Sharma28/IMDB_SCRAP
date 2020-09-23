# import json
# import requests 
# from bs4 import BeautifulSoup
# from pprint import pprint
# file = open('deepak.json', 'r')
# data = json.load(file)
# Counter = 0
# details_of_movie = []
# for i in data :
#     url = i['Url']
#     response = requests.get(url)
#     Soup = BeautifulSoup(response.text , "html.parser")





#     Movies = {}
#     div = Soup.find('div' , class_ = 'title_wrapper').h1.get_text()
#     movie_name = ''
#     Movie_details = []
#     for i in div :
#         if i != '\xa0' :
#             movie_name+=i
#         else:
#             break
#     # Movie_details.append(movie_name)
#     Movies['Movie'] = movie_name





#     sub_text = Soup.find('div', class_='subtext')
#     time = sub_text.find('time').text.strip()
#     list_ = list(time)
#     Duration = ''
#     for i in list_ :
#         if i != "h" :
#             Duration+=i
#         else:
#             break    
#     Duration = int(Duration)
#     time_ = Duration*60
#     a = time_
#     b = ''
#     for i in range(len(list_)):
#         index_ = i - len(list_)
#         if list_[index_] in "0123456789" :
#             b+=list_[index_]
#         elif list_[index_] == "h" :
#             break
#     time_of_movie = a+int(b)
#     # Movie_details.append(time_of_movie)
#     Movies['Runtime'] = time_of_movie




#     gener = sub_text.find_all('a')
#     list_of_gener = []
#     for i in gener :
#         list_of_gener.append(i.text)
#     list_of_gener.pop()
#     # Movie_details.append(list_of_gener)
#     Movies['Genre'] = list_of_gener





#     summary = ''            
#     div_ = Soup.find('div' , class_ = 'plot_summary')
#     bio = div_.find('div' , class_ = 'summary_text')
#     summary += bio.text.strip()
#     # Movie_details.append(summary)
#     Movies['summary'] = summary






#     credit_summary_item = div_.find_all('div' , class_ = 'credit_summary_item')
#     Directors = []
#     for i in credit_summary_item :
#         if "Director" in i.text :
#             Director = i.find_all('a')
#             for j in Director :
#                 Directors.append(j.text)
#     # Movie_details.append(Directors)
#     Movies['Director'] = Directors






#     div__ = Soup.find('div' , class_ = 'poster')
#     Poster = div__.find('a')
#     images= Poster.find("img")['src']
#     # Movie_details.append(images)
#     Movies['Image'] = images





#     div1_ = Soup.find_all('div' , class_ = 'txt-block')
#     languages = []
#     for i in div1_:
#         if "Country" in i.text :
#             Country= i.find("a").text
#             # Movie_details.append(Country)
#     Movies['Country'] = Country
#     for i in div1_  :
#         if "Language" in i.text :
#             Language = i.find_all("a")
#             for j in Language :
#                 languages.append(j.text)   
#     # Movie_details.append(languages)
#     Movies['Languages'] = languages
#     details_of_movie.append(Movies)
#     Counter += 1 
#     if Counter == 10 :
#         break
# file = open('data_of_task5.json','w')
# data = json.dump(details_of_movie , file , indent = 4)




# import json
# from pprint import pprint
# All_details_of_movie = []
# Group_of_details = {}
# file = open('deepak.json','r')
# data = json.load(file)
# file_ = open('data_of_task4.json','r')
# data_ = json.load(file_)
# # print(data_)
# Counter = 0
# Group_of_details = []
# for i in data:
#     dict1={}
#     for j,k in i.items():
#         if k not in dict1 :
#             dict1[j] = k
#     Group_of_details.append(dict1)
# l=0
# for x in data_ :

#     for y,z in x.items() :
#         Group_of_details[l][y]=z
#     l+=1
# pprint(Group_of_details[:10])
    # if Counter == 10 :
    #     break
    # else:
    #     Counter+=1
# pprint(Group_of_details)             
    # # All_details_of_movie.append(Group_of_details)
# pprint(All_details_of_movie)    

# dic={"name":"deepak","time":"raj","bio":"raj"}
# dic1={}
# for i in dic:
#     dic1["time"]=dic[i]
#     dic1["bio"]=dic[i]
# print(dic1)
































































































# import requests 
# from bs4 import BeautifulSoup 
# response = requests.get('https://www.imdb.com/india/top-rated-indian-movies/')
# Soup = BeautifulSoup(response.text , 'html.parser')
# tbody = Soup.find('tbody' , class_ = 'lister-list')
# trs = tbody.find_all('tr')
# counter = 0
# for i in trs :
#     Movies = []
#     if counter == 10 :
#         break
#     td = i.find('td' , class_ = 'titleColumn').text.strip()
#     for j in td :
#         if j != '.' :
    # Number = ''
    # for j in titleColumn :
        # print(j.text)
        # if position != '.' :
        #     Number+=position
        # else:
        #     print(Number)     
    # counter+=1
    # print(tds)
    # for j in tds :
        # print(j) 

# for i in tr :

