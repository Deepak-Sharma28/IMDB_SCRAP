import json
from pprint import pprint
file = open('details2.json', 'r')
data = json.load(file)
Directors = []
Details = {}
Directors_without_list = []
for i in data :
    if i['Director'] not in Directors :
        a = i['Director']
        Directors.append(i['Director'])
        for j in a :
            Directors_without_list.append(j)


for i in Directors_without_list :
    Details[i] = {}       
Language = []


for i in data :
    for j in i :
        a = (i['Languages'])
        for x in a :
            if x not in Language :
                Language.append(x)                              

for i in Directors_without_list :
    for r in Language :
        c = 0 
        for x in data :    
            for j in x['Director'] :
                if j == i :
                    for t in x['Languages'] :
                        if t == r :
                            c+=1
        if c>0 :
            for n in Details :
                if n == i :
                    Details[n][r] = c

file = open('data_of_task10.json','w')
data = json.dump(Details , file , indent = 4)

print(Details)

                    