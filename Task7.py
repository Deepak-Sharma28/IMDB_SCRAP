import json
file = open('details2.json', 'r')
data = json.load(file)

Directors = []
Counter = 0
for i in data :
    Counter += 1
    if Counter == 10 :
        break
    Directors.append(i['Director'])
Director = []
for i in Directors :
    for j in i :
        if j not in Director :
            Director.append(j)
Dict = {}
for i in Director :
    Counter = 0
    for j in Directors :
        if i in j :
            Counter += 1
            Dict[i] = Counter 
print(Dict)                                      
