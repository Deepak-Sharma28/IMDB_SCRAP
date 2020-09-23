# import json
# from pprint import pprint
# file = open("deepak.json","r+")
# data_of_Task_1 = json.load( file)  
# dict1 = {}
# Years=[]
# Group_of_Movies = []
# c=0
# for i in data_of_Task_1 :
#     year = i["Year"]
#     if year not in List :
#         List.append(year)
#         lis = []        
#         for j in data_of_Task_1 :
#             if year == j["Year"] :
#                 lis.append(j)
#         Group_of_Movies.append(lis)
# pprint(Group_of_Movies)


# for i in data_of_Task_1 :
#     year = i["Year"]
#     if year not in Years :
#         Years.append(year)
#     Movie_dic = {i : [] for i in Years}
# # pprint(data_of_Task_1)    
# for i in data_of_Task_1 :
#     years = i["Year"]
#     for j in Movie_dic :
#         if str(j) == str(years) :
#             Movie_dic[j].append(i)
# pprint(Movie_dic)

 
# file = open("data_of_task2.json","w") 
# data = json.dump(Movie_dic , file , indent = 4)
# file.close()
                


        
















