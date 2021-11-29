# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)
# #######################################

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])
# #########################################

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)
# ##########################################

# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
# print(thisdict)
# ############################################

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(type(thisdict))
# ############################################
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"]
# print(x)
# ###############################################

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.get("model")
# print(x)
# #################################################

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.keys()
# print(x)
# ###################################################

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.keys()
# print(x) 
# car["color"] = "white"
# print(x)
# ###################################################

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.values()
# print(x)
# ###################################################

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.values()
# print(x)
# car["year"] = 2020
# print(x)
# ###################################################

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.values()
# print(x)
# car["color"] = "red"
# print(x) 
# ####################################################

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.items()
# print(x)
# ##################################################

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")
#   ####################################################################

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2018
# print(thisdict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})
# print(thisdict)
# #########################################################################

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"color": "red"})
# print(thisdict)
# ########################################################################

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)

# hisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)
# ##############################################################

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict:
#   print(x)

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict:
#   print(thisdict[x])

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict.values():
#   print(x)

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict.keys():
#   print(x)

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x, y in thisdict.items():
#   print(x, y)
#####################################################################

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisdict)
# print(mydict)
# ###################################################################

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# print(myfamily)
# #########################################################################

# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

# print(myfamily)
# #################################################################

################### Meraki solve qestion ##############################

# city_population = {
#     "NewYorkCity":8550405,
#     "LosAngeles":3971883, 
#     "Toronto":2731571, 
#     "Chicago":2720546, 
#     "Houston":2296224, 
#     "Montreal":1704694, 
#     "Calgary":1239220, 
#     "Vancouver":631486, 
#     "Boston":667137
# }
# print(city_population["NewYorkCity"])
# print(city_population)
# print(type(city_population))
#################################################################

# dict = {
#     'ball':"green",
#     'Ball':'red' 
# }
# print(dict['ball'])
# print(dict['Ball'])
# print(dict['bat'])
##################################################################
# dict = {
#     'name':'ravina',
#     'age':'20'
# }
# print(dict['age'])
# print(dict['name'])
###############################################################

# my_dict = {
#     1: 'apple',
#     2: 'ball'
# }
# x = my_dict.keys()
# print(x)
# ##############################################################

# my_dict = {
#     'name': 'John',
#      1: [2, 4, 3]
#     }
# print(my_dict['name'])
# print(my_dict[1])
# ###############################################################

# Dic= {
#  1: 'NAVGURUKUL',
#  2: 'IN',  
#  3:{
#      'A' : 'WELCOME',
#      'B' : 'To', 
#      'C' : 'DHARAMSALA'
#      }
# }
# print(Dic)
############################ Accessing elements methode #####################################

# person = {
#     "name":"jack",
#     "age":20,
#     "gender":"male",
#     4:"organistion"}
# result = person['age']
# x =  person.get("gender")
# print(person[4])
# print(x)
# print(result)

# person={
#     'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:{
#         'organisation':'navgurukul','place':'dharamsala'
#         }
#     }
# print(person['gender'])
# print(person[4])
# result = person[4]['place']
# print(result)
##################### Adding methode #################################
# dic= {
#     'Name': 'RAM', 
#     'Age': 17,
#     }    
# dic['ORGANIZATION'] = "NAV GURUKUL"
# dic['place'] = 'dharamsala'
# print(dic)

# dic= {
#     'Name': 'RAM',
#     'Age': 17,
#      }
# dic['student']={
#         'id':22, 
#         'place':'dharamsala'
#     }
# print(dic)

# car ={
#     "brand":  "ford",
#     "model":  "mustang",
#     "year":  1964
# }
# if "model" in car:
#     print("Yes, 'model' is one of the keys in the car dictionary.")

# else:
#     print("No, 'model' key dictionary mai nahi hai.")
# ######################## Update methode ##################################

# details={
#     'Name': 'RAM',
#      'Age': 17, 
#      'student': {
#       'id': 22,
#       'place': 'dharamsala'
#       }
#      } 
# details['student']['id']=35
# print(details); 

# classes ={
#     "room1":  "6th",
#     "room2":  "7th",
#     "room3":  "8th"
#         }
# mydict=classes.copy()
# print(mydict)
# ######################### Remove mothode#####################################

# CAR_DETAILS={
#     "brand": "Ford",
#     "model": "jason",
#     "year": 1964
# }
# CAR_DETAILS.pop("model")
# print(CAR_DETAILS)

# person={
#     'name':'jack',
#     'id':22,
#     'place':'dharamsala'
# }
# person.popitem()
# print(person)

# person={
#     'name':'jack',
#     'id':22,
#     'place':'dharamsala'
# }

# del person['place']
# print(person)
# ########################## Iteration elements ###################################

# states_capitals = {
#     'Gujarat' : 'Gandhinagar',
#     'Maharashtra' : 'Mumbai',
#     'Rajasthan' : 'Jaipur',
#     'Bihar' : 'Patna'
#     }
# for state in states_capitals:
#         print(state)


# states_capitals = {
#     'Gujarat' : 'Gandhinagar',
#     'Maharashtra' : 'Mumbai',
#     'Rajasthan' : 'Jaipur',
#     'Bihar' : 'Patna'
#     }    
# for state in states_capitals:
#     print(states_capitals[state])

# details ={
#     "name":  "Bijender",
#     "age":  17,
#     "class":  "10th"
#     }
# for x in details.values():
#     print(x)

# movie ={
#     "name":  "Puli",
#     "hero":  "Vijay",
#     "rating":  7.5
#     }
# for x,y in movie.items():
#     print(x,y)

# meal ={
#     "monday":  "Chole chawal",
#     "sunday":  "Fried rice",
#     "wednesday":  "dosa"
#     }
# print(len(meal))
# #########################################################################

####################### Meraki Question ##################################

# dict1={1:10, 2:20}
# dict2={3:30, 2:40}
# dict3={5:50, 6:60}
# dict4={}
# for i in dict1:
#     if i in dict2:
#         dict1[i]=dict1[i]=dict2[i]
# dict4={**dict2,**dict1,**dict3}
# print(dict4)
# ###################### Q2 ##############################################

# dict={"name":"Raju", "marks":56}
# b = input("enter the key:--  ")
# if b in dict:
#     print("key present in the dictionary")
# else:
#     print("key is no present in the dictionary")
####################### Q3 ###############################################

# my_dict = {
#     'data1':100,
#     'data2':-54,
#     'data3':247
# }
# print(sum(my_dict.values()))
# ######################## Q4 ############################################

# dict = {
#     1:'NAVGURUKUL',
#     2:'IN',
#     3:{
#         'A':'WELCOME',
#         'B':'TO',
#         'C':'DHARAMSHALA'
#     }
# }
# for a,b in dict.items():
#     if a==3:
#         x=b
#         x.pop("A")
# print(dict)
# ########################## Q5 ##########################################

# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5,]
# dict={}
# for s in range(len(list1)):
#     dict.update({list2[s]:list1[s]})
# print(dict)
# ########################### Q6 ##########################################

# dic={
#     'ball':'red',
#     'bat':4,
#     'wickets':8,
#     'ball':'green',
#     'bat':3
#     }
# di={}
# for j in dic.items():
#     print(j)
# ########################### Q7 #############################################

# a=[
#     {"first":"1"},
#     {"second":"2"},
#     {"third":"1"},
#     {"four":"5"},
#     {"five":"5"},
#     {"sex":"9"},
#     {"seven":"7"}
# ]
# b=[]
# for i in a:
#     for j in i.values():
#         if j not in b:
#             b.append(j)
# print(b)
############################## Q8 ###########################################

# a = {}
# user = int(input("Number of Elements:--  "))
# for i in range(user):
#     k = input("Enter key:--  ")
#     v = input("enter value:--  ")
#     a.update({k:v})
# print(a)
# ############################# Q9 ###########################################

# a='mississippi'
# dict={}
# b=[]
# c=0
# d=0
# e=0
# f=0
# for i in a:
#     if "m" == i:
#         c+=1
#     if "s" == i:
#         d+=1
#     if "i" == i:
#         e+=1
#     if "p" == i:
#         f+=1
# dict['m']=c
# dict['s']=d
# dict['i']=e
# dict['p']=f
# # print(dict) 
# user =input("Enter a Name:--  ")
# a=[]
# b=[]
# dict={}
# for r in user:
#     a.append(r)
#     for s in a:
#         b.append(s)
#     dict.update({})    
# print(dict)
# ############################ Q10 ############################################        

# dict =  {
#    'Alex': ['subj1', 'subj2', 'subj3'], 
#    'David': ['subj1', 'subj2'],
#    "roshan": ["maniram","kanta"],
#    'satish':"x",
#    'akash':'pradeep',
# }

# count=0
# for i in list(dict.values()):
#       if type(i)==list:
#             for j in i:
#                   count+=1
#       else:
#             count+=1
# print(count)
# ############################# Q11 ###############################################
# from collections import Counter
# my_dict = {
#     'a':50, 
#     'b':58, 
#     'c':56,
#     'd':40, 
#     'e':100, 
#     'f':20
# }
# k=Counter(my_dict)
# high = k.most_common(3)
# print("Dictionary with 3 highest values:")
# # print("values")
# for i in high:
#        print(i[1]," ")
# ############################# Q12 ###############################################
       
# user = int(input("Enter the number:--  "))
# dict = {}
# for i in range(1,user+1):
#        dict.update({i:i*i})
# print("dictionary of square",dict)
# ############################ Q13 #################################################
# from collections import Counter
# my_dict = {
#     'a':50, 
#     'b':58,
#     'c':56,
#     'd':40,
#     'e':100, 
#     'f':20
# }
# k = Counter(my_dict)
# high = k.most_common(3)
# print("dictionary with 3 highest keys")
# print("key")
# for i in high:
#        print(i[0]," :")
############################### Q14 ##############################################

# import operator
# dict1 = {'param':20,'anjili':30,'bijender':45,'roshini':50,'deepak':60}
# s = dict(sorted(dict1.items(),key=operator.itemgetter(1)))
# print("asecending order:",s)
# s1 = dict (sorted(dict1.items(),key=operator.itemgetter(1),reverse=True))
# print("descending order:",s1)
# ###########################################################################
################################ Dictionary Code Output ###########################

# a = {(1,2):1,(2,3):2}
# print(a[1,2])
# # options
# A. Key Error

# B. 1         currect
# C. {(2,3):2}
# D. {(1,2):1}
# ####################### Q2 ######################################

# a = {'a':1,'b':2,'c':3}
# print (a['a','b'])

# # Options 
# # A. Key Error  currect
# # B. [1,2]
# # C. {‘a’:1,’b’:2}
# # D. (1,2)
# ############################ Q3 ####################################

# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1        
# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')
# print (len(fruit))
# print(fruit)
# ############################## Q4 ###################################

# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age
# print (len(Details["Student"])) 
# ########################## Q5 #######################################

# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12

# sum = 0
# for k in my_dict:
#     sum += my_dict[k]

# print (sum)
# print(my_dict)
# ############################# Q6 #######################################

# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print (len(crates[box]))

# output TypeError
############################ Q7 ###########################################

# rec = {
# "Name" : "Python", 
# "Age":"20",
# "Addr" : "NJ", 
# "Country" :"USA"
# }
# id1 = id(rec)
# del rec

# rec = {
#     "Name" : "Python", 
#     "Age":"20", 
#     "Addr" : "NJ", 
#     "Country" : "USA"
#     }
# id2 = id(rec)
# print(id1 == id2)

# output True
# ########################### Dictionary Debug Code ############################################# 

# c
# details={
#     "name":"Roshan",
#     "age":23,
#     "last":"Lale",
#     "email":"shanti@navgurukul.org",
#     }

# print(details["name"])
# print(details["last"])
# print(details["age"])
# ############################ Q2 ################################################################

# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1.values():    
#    sum=sum+1     #sum=sum+=i currect
# print(sum)
############################# Q3 ###############################################################

# c=dict()
# for i in range(1,16):
#     c.update({i:i*i})
# print(c)
# ############################# Q4 ############################################################# 

# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}
# c={}
# for i in (s,a):
#     c.update(i)
# print(c)
# ##########################################################################################

######################## W3 resource questions ###########################

# dict={0:10, 1:20}
# dict.update({2:30})
# print(dict)
############################# Q2 ###############################################

# dict={1:10, 2:20, 3:30, 4:40}
# def is_key_present(x):
#     if x in dict:
#         print("key is present in the dictionary")
#     else:
#         print("key is not present in the dictionry")
# is_key_present(4)
# is_key_present(5)
# ########################## Q3 #####################################################

# user=int(input("enter a number:---  "))
# dict={}
# for i in range(1,user+1):
#     dict[i]=i*i
# print(dict)
# ########################## Q4 #####################################################

# dict={}
# for i in range(1,10):
#     dict[i]=i**2
# print(dict)
# ########################## Q5 ########################################################

# dict1 = {'a':100, 'b':200}
# dict2 = {'s':300, 'r':200}
# d = dict1.copy()
# d.update(dict2)
from typing import ItemsView


a = {}
# user = int(input("Number of Elements:--  "))
# for i in range(user):
#     k = input("Enter key:--  ")
#     v = input("enter value:--  ")
#     a.update({k:v})
# print(a)ta3':247}
# total=1
# for i in my_dict:
#     total=total*my_dict[i]
# print(total)
# ########################### Q12 #########################################################

# my_dict = {'a':1,'b':2,'c':3,'d':4}
# if 'a'in (my_dict):
#     del my_dict['a']
# print(my_dict)
# ########################### Q13 ###########################################################

# keys = ['red', 'green', 'blue']
# values = ['Roshan','Akash', 'Satish']
# dict1 = dict(zip(keys, values))
# print(dict1)
# ############################# Q14 #########################################################

# dict = {'red':'Roshan',
#         'green':'Akash',
#         'black':'Satish',
#         'white':'Amit'}
# for i in sorted(dict):
#     print((i, dict[i]))
# ############################## Q15 #########################################################

# my_dict = {'x':500, 'y':5874, 'z': 560}
# keys_max=max(my_dict.keys())
# keys_min=min(my_dict.keys()) 
# print('maximum value',my_dict[keys_max])
# print('minmum value',my_dict[keys_min])
################################## Q16 #######################################################

# class dict():
#     def __init__(self):
#         self.x = 'red'
#         self.y = 'Yellow'
#         self.z = 'Green'
#     def nothing(self):
#         pass
# test = dict()
# print(test.__dict__)
# ############################### Q17 ###########################################################

# student_data = {'id1': 
#    {'name': ['Sara'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
#  'id2': 
#   {'name': ['David'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
#  'id3': 
#     {'name': ['Sara'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
#  'id4': 
#    {'name': ['Surya'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
# }
# result = {}
# for key,value in student_data.items():
#     if value not in result.values():
#         result[key] = value
# print(result)
# ############################### Q18 ###############################################################

# dict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# dict.clear()
# print(dict)
# ############################### Q19 ##############################################################


# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3 = {}
# for i, j in d1.items():
#     for x, y in d2.items():
#         if i == x:
#             d3[i]=(j+y)
# print(d3)

# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# print("\U0001f600")
# print("\U0001F606")
# print("\U0001F923")
# print("\N{grinning face}")
# print("\N{slightly smiling face}")
# print("\N{winking face}")
############################################################################################################
# a = {}
# b=0
# # user = int(input("Number of Elements:--  "))
# for i in range(b):
#      k = input("Enter key:--  ")
#      v = input("enter value:--  ")
#      a.update({k:v})
# print(a)
###########################################################################################################
# emp = ['emp1','emp2']
# a = ["Name","Age","Salary"]
# b = ["Roshan","Satish"]
# c = [23,19]
# d = [30000,50000]
# e = []
# b = dict(zip(b,c))
# y = 0
# for i,r in b.items():
#     e.append({a[0]:i,a[1]:r,a[2]:d[y]})
#     y+=1
# print(e)

# dict={"name":"Roshan","name":"satish"}
# dict1={}
# for i,r in dict.items():
#     dict1[r]=i
# print(dict1)

