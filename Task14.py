import json
from pprint import pprint
file = open('cast.json','r')
data = json.load(file)
actors_id = {}

for i in data :
    for j in range(len(i)-1) :
        Actor = i[j]['Name']
        co_actor = (i[j+1]['Name'])
        imdb_id = i[j]['imdb_id']
        imdb_id_ = (i[j+1]['imdb_id'])
        frequent_co_actor = []
        Co_actor = {}
        actor = {}
        Co_actor['imdb_id'] = imdb_id_
        Co_actor['name'] = co_actor
        c =0
        for n in data :
            if i[j] in n and i[j+1] in n :
                c+=1
        Co_actor['num_movies'] = c
        frequent_co_actor.append(Co_actor)
        actor['name'] = Actor
        actor['frequent_co-actor'] = frequent_co_actor
        actors_id[imdb_id] = actor


        