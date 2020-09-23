import requests , json #imported requests and json modules 
from bs4 import BeautifulSoup #imported beautifulSoup 
from pprint import pprint #imported preety print
url = "https://www.imdb.com/india/top-rated-indian-movies/" #url of top 250 movies
Soup = BeautifulSoup(response.text,"html.parser") #parsing the response via beautifulSoup


import os.path  #imported os module  


if os.path.isfile("deepak.json") : #checking the file exists or not
    file = open("deepak.json","r")
    data_ = json.load(file)
    print("exists")
else:    
    url =  "https://www.imdb.com/india/top-rated-indian-movies/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text , "html.parser")

    div = soup.find('div' , class_ ='lister')
    tbody = div.find('tbody' , class_ = 'lister-list')
    trs=tbody.find_all('tr') 
    
    
    '''all the details of the movies is exists in tbody
    that is why i have taken all the tr tags in trs'''



    Rank_of_Movie = [] #rank of movie
    Name_of_Movie = [] #name of movie
    Year_of_releasing = [] #year of releasing
    Url_of_Movie = [] #url of movie
    Rating_of_Movie = [] #rating of movie

    for tr in trs :
        Position = tr.find('td' , class_= 'titleColumn').get_text().strip()
        #by get text function i am getting all the texts from td of titlecolumn and with strip i can erase white spaces
        Rank = ''
        for i in Position :
            if '.' not in i :
                Rank+=i
            else:
                break
        
        # i am getting all the details from given tags of given classes
        Rank_of_Movie.append(Rank)        
        title = tr.find('td' , class_='titleColumn').a.get_text()
        Name_of_Movie.append(title)
        release = tr.find('td' , class_='titleColumn').span.get_text()
        Year_of_releasing.append(release)
        Rating = tr.find('td' , class_='ratingColumn imdbRating').strong.get_text()
        Rating_of_Movie.append(Rating)
        Link = tr.find('td' , class_='titleColumn').a['href']
        Movie_link = "https://www.imdb.com"+Link
        Url_of_Movie.append(Movie_link)
    Top_Movies = []


    #here i am running loop on the ranks of the movies and saving data in a dict and append it in a list 
    for i in range(len(Rank_of_Movie)):
        details = {}
        details['Position'] = int(Rank_of_Movie[i])
        details['Name'] = str(Name_of_Movie[i])
        Year_of_releasing[i] = Year_of_releasing[i][1:5]
        details['Year'] = int(Year_of_releasing[i])
        details['Rating'] = float(Rating_of_Movie[i])
        details['Url'] = Url_of_Movie[i]     
        Top_Movies.append(details)
file = open("deepak.json","w+")
data_of_Task_1 = json.dump(Top_Movies, file , indent = 4)
