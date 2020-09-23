import json
from pprint import pprint
Language = []
Languages_of_all = []
file = open('details2.json' , 'r')
data = json.load(file)
c = 0
for i in data :
    Languages = []
    for j in i :
        a = (i['Languages'])
        Languages_of_all.append(a)
        for x in a :
            if x not in Language :
                Language.append(x)
        break
# print(Languages_of_all)
# print(Language)

Dict = {}
c = 0
for i in Language :
    Counter = 0
    for j in Languages_of_all :
        if i in j :
            Counter += 1
            c+=1    
    Dict[i] = Counter
print(Dict)            



