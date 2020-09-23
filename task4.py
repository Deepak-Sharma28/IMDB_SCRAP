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
#     Movies['Name'] = movie_name





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
# file = open('data_of_task4.json','w')
# data = json.dump(details_of_movie , file , indent = 4)
# print(details_of_movie)            

# Movies = {"Movie" , "Runtime ", "Genre" , "Bio" , "Director" , "Poster_ url" , "Language" }
# for i in Movies :
    # c = 0 
    # Movies[i] = Movie_details[c]
    # c+=1
# print(Movies)
    

# dict_ = '{"Name" : ["Deepak" ], "Class" : [12] , "DOB" : ["27/10/1999"]}'
# user = input()
# if user == "Add" :

# file  = open('extra.json','w')
# data = json.dump(dict_ , file , indent=4)
# print(type(data))

# user = input()
# file_ = open('extra.json','r')
# data = json.loads(dict_)
# user = input("what do you want Add and Remove")
# if "Add" in user :
#     user_ = input("What do you want add Name , Class or DOB ?")
#     user__ = input("What do you want To add")
#     if user_ not in data :
#         data[user_] = user__
#         print(data)
#     else:
#         for i in data :
#             if i == user_ :
#                 # user__ = input("Add what you want to ?")
#                 data[i].append(user__)
#         print(data)        
#     # file = open("extra.json" , "w")
#     # data1 = json.dump(data , file , indent = 4)        
# elif "Remove" in user :
#     user_ = input("what do you want remove Name , Class or DOB ?")
#     user__ = input("What do you want to remove")
#     if user_ not in data :
#         data[user_] = user__
#         for i in data :
#             if i == user_ :
#                 # user__ = input("remove what do you want to ?")
#                 data[i].remove(user__)
#         print(data)        



