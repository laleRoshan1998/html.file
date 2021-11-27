# names_list=["roshan","akash","amit","rajkumar"]
# print (names_list)
# print (type(names_list))
# #################################################

# marks_list=[70,80,75,65,68]
# print(marks_list)
# print(type(marks_list))
# ###################################################

# mixed_list=["roshan",12, 9.0, "kaavay","satish",1]
# print (type(mixed_list))
# #####################################################

# names_list=["annu","roshan","akash","satish","amit"]
# print (names_list[1])
# #######################################################

# names_list=["annu","shivam","deepa","rupa","pooja"]
# print (names_list[0])
# print (names_list[4])
# ############################################################

# names_list=["roshan","akash","satish","amit"]
# print(names_list[0])
# ######################################################

# names_list=["roshan","akash","satish","amit","amol"]
# print(len(names_list))
########################################################

# names_list=["roshan","amol","alok","satish","akash"]
# print(names_list.append("alok"))
# print("lenght of the list is",len(names_list))
# print(names_list)
# #####################################################

# names_list=["annu","shivam","deepa","pooja","rupa","dhruv","alok"]
# names_list.pop()
# print("lenght of the list is ",len(names_list))
# print(names_list)
# #########################################################

# names_list=["roshan","satish","akash","amit","amol","rajkumar"]
# names_list.pop()
# print("lenght of the list is",len(names_list))
# print(names_list)
# ##########################################################

# names_list=["roshan","akash","satish","amit","shivam"]
# print("lenght of the list is ",len(names_list),names_list)
# names_list.pop(2)
# print("lenght of the list is", len(names_list),names_list)
# names_list.pop(2)
# print("lenght of the list is ",len(names_list),names_list)
# ##########################################################

# student_list=["roshan","akash","amit","amol","pradeep","khawaja"]
# list_lenght=len(student_list)
# index=0
# while index < list_lenght:
# 	print(student_list[index])
# 	index+=1
# #############################################################

# student_marks=[23,45,89,90,56,80]
# lenght=len(student_marks)
# index=0
# total_marks=0
# while index < len(student_marks):
# 	total_marks=student_marks[index]+total_marks
# 	index+=1
# print("total_marks: "+str(total_marks))
# ##############################################################

# student_marks=[23,45,67,89,90,54,34,23,19,28,10,45,86,87,9]
# list_lenght=len(student_marks)
# index=0
# less_than50=0
# more_than50=0
# while index < list_lenght:
# 	marks=student_marks[index]
# 	if marks<50:
# 		less_than50=less_than50+1
# 	else:
# 		more_than50=more_than50+1
# 	index+=1
# print("marks more than50: "+str(more_than50))
# print("marks less than 50: "+str(less_than50))
# ###################################################################

# thislist=["apple","banana","cherry","orange","kiwi","mango"]
# print(thislist[2:4])
####################################################################

# thislist=["apple","banana","cherry"]
# thislist[1]="blackcurrant"
# print(thislist)
################################################################

# thislist=["apple","banana","cherry"]
# thislist.insert(2,"watermelon")
# print(thislist)
# ###################################################################

# thislist=["apple","banana","cherry"]
# tropical=["mango","pineapple","papaya"]
# thislist.extend(tropical)
# print(thislist)
####################################################################

# thislist=["apple","banana","cherry"]
# thistuple=["kiwi","orange"]
# thislist.extend(thistuple)
# print(thislist)
# ####################################################################

# list1=["a","b","c"]
# list2=[1,2,3]
# for x in list2:
# 	list1.append(x)
# print(list1)
# #####################################################################

# thislist=["apple","banana","cherry"]
# thislist.remove("banana")
# print(thislist)
# #######################################################################

# thislist=["apple","banana","cherry"]
# thislist.pop(0)
# print(thislist)
# ############################################################################

# thislist=["apple","banana","cherry"]
# thislist.clear()
# print(thislist)
# #######################################################################

# thislist=["apple","banana","cherry"]
# for x in thislist:
# 	print(x)
# ########################################################################

# thislist=["apple","banana","cherry"]
# for i in range(len(thislist)):
# 	print(thislist[i])
# #########################################################################

# thislist=["apple","banana","cherry"]
# i=0
# while i < len(thislist):
# 	print(thislist)
# 	i+=1
##########################################################################

# fruits=["apple","banana","cherry","kiwi","mango"]
# newlist=[]
# for x in fruits:
# 	if "a" in x:
# 		newlist.append(x)
# print(newlist)
# #########################################################################

# fruits=["apple","banana","cherry","kiwi","mango"]
# newlist=[x for x in fruits if "a" in x]
# print(newlist)
# ##########################################################################

# fruits=["apple","banana","cherry","kiwi","mango"]
# newlist=[x for x in fruits if x !="apple"]
# print(newlist)
############################################################################

# fruits=["apple","banana","cherry","kiwi","mango"]
# newlist=[x for x in fruits]
# print(newlist)
# ############################################################################

# newlist=[x for x in range(10)]
# print(newlist)
# ############################################################################

# fruits=["apple","banana","cherry","kiwi","mango"]
# newlist=[x.upper()for x in fruits]
# print(newlist)
# #############################################################################

# fruits=["apple","banana","cherry","kiwi","mango"]
# newlist=[x if x !="banana" else "ornge" for x in fruits]
# print(newlist)
# #############################################################################

# thislist=["orange","mango","kiwi","pineapple","banana"]
# thislist.sort()
# print(thislist)
###############################################################################

# thislist=[100,50,65,82,23]
# thislist.sort()
# print(thislist)
# ###############################################################################

# thislist=["ornge","mango","kiwi","pineapple","banana"]
# thislist.sort(reverse=True)
# print(thislist)
# #################################################################################

# thislist=[100,50,65,82,23]
# thislist.sort(reverse=True)
# print(thislist)
# ##################################################################################

#def myfunc(n):
#   return abs(n - 50)
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)
# ##################################################################################

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)
# #################################################################################

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)
# ##################################################################################

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)
# ###################################################################################

# thislist = ["apple","banana","cherry"]
# mylist = thislist.copy()
# print(mylist)
# ###################################################################################

# thislist = ["apple","banana","cherry"]
# mylist = list(thislist)
# print(mylist)
# ###################################################################################

# list1 = ["a","b","c"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)
#####################################################################################

# list1 = ["a","b","c"]
# list2 = [1, 2, 3]
# for x in list2:
#   list1.append(x)
# print(list1)
# #####################################################################################

# list1 = ["a","b","c"]
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1)
# ####################################################################################

# students_list = ["robin", "anamika", "faisal", "valmiki", "waseem", "amara"]
# list_length = len(students_list)
# index = 0
# while index < list_length:
#     print(students_list[index])
#     index = index + 1
#####################################################################################

# student_marks=[23,45,89,56,80]
# lenght=len(student_marks)
# index=0
# total_marks=0
# while index<len(student_marks):
#   total_marks=student_marks[index]+total_marks
#   index=index+1
# print(total_marks: +str(total_marks)
# #####################################################################################

# student_marks=[23,45,67,89,54,34,21,34,23,19,28,10,45,86,87,9]
# list_lenght=len(student_marks)
# index=0
# less_than50=0
# more_than50=0
# while index<list_lenght:
#   marks=student_marks[index]
#   if marks<50:
#     less_than50=less_than50+1
#   else:
#     more_than50=more_than50+1
#   index+=1
# print("marks more than 50:"+str(more_than50))
# print("marks less than 50:"+str(less_than50))
# ########################################################################################

#####################meraki question ####################################################

# numbers=[50,40,23,70,56,12,5,10,7]
# # a=len(numbers)
# count=0
# for i in numbers:
#   count+=1
# print(count)
# ########################################################################################

# numbers=[50,40,23,70,56,12,5,10,7]
# count=0
# for i in (numbers):
#   if i>20 and i<=40:
#     count+=1
# print(count)
# ########################################################################################

# numbers=[50,40,23,70,56,12,5,10,7]
# numbers.sort()
# print(numbers)
# print("first numbers maximum",numbers[-1])
# print("second numbers maximum",numbers[-2])
# print("third numbers maximum",numbers[-3])
# ########################################################################################

# places=["delhi","gujrat","rajstan","punjab","kerala"]
# places.reverse()
# print(places)
# list_lenght=len(places)
# index=0
# while index < list_lenght:
#   print(places[index])
#   index+=1
# #########################################################################################

# name=['n','i','t','n']
# name.reverse()
# print(name)
# list_lenght=len(name)
# index=0
# while index < list_lenght:
#   print(name[index],end=" ")
#   print(end="\n")
#   index+=1
# ##########################################################################################

# user=input("enter the decimal number:--  ")
# l=[]
# while (user!=0):
#   a=user%2
#   l.append(a)
#   user=user//2
# l.reverse()
# print(l)


# user=int(input("enter the binary number:--  "))
# final=0
# l=0
# while user!=0:
#   a=user%10
#   a=a*2**l
#   l+=1
#   final+=a
#   user=user//10
#   print(final)
###################### Nested Lists #########################################################
############################################################################################

# str2="Roshan"
# str2lst=list(str2)
# print(str2lst)

# a="roshan"
# l=list(a)
# print(l)
# ############################################################################################

# list1=[1,2,3,4,5,6]
# list2=[2,3,1,0,6,7]
# list3=[]
# for i in range(len(list1)):
#   if i not in list2:
#     list3.append(i)
# print(list3)
##############################################################################################
# ###############################################################################E############

# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78]
# ]
# total=0
# a=marks[0]+marks[1]+marks[2]
# for i in a:
#   total+=i
# print(total)
# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65, 76],
#     [95, 45, 78, 52, 49]
# ]

# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78]
# ]

# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78],
#     [87, 67, 49, 68, 88]
# ]

# t=0
# for s in marks:
#   for v in s:
#     t+=v
# print(t)
# ######################################################################################

# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65, 76],
#     [95, 45, 78, 52, 49]
# ]

# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78]
# ]

# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78]
#]


# for i in range(len(marks)):
#   lenght=len(marks[i])
#   sum1=0
#   for a in marks[i]:
#     sum1+=a
#   b=sum1//lenght
#   print(b)

##############################################################################

# number=30
# n=[10,11,12,13,14,17,18,19]
# a=[]

# for i in n: 
#   for r in n:
#     b=i+r
#     if b==number:
#       if [i,r] not in a and [r,i] not in a:
#         a.append([i,r])
# print(a)
# ############################################################################

# magic_square = [
#     [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]
# ]

# for r in magic_square:
#   s=0
#   for c in r:
#     s+=c
#   print(s)
# #############################################################################

# student=['Rishabh','Madhurima','rahul','Abhishek','Faizal','Muskaan']
# marks=[10,20,56,45,36,20]
# lenght=len(student)
# index=0
# while index<lenght:
#   print(student[index],marks[index])
#   index+=1
# ###############################################################################

# elements=[23,14,56,12,19,9,15,25,31,42,43]
# even=0
# odd=0
# for i in elements:
#   if i%2==0:
#     even+=1
#   if i%2!=0:
#     odd+=1
# print('this is the ',even)
# print('this is the', odd)
# ################################################################################

# elements=[23,14,56,12,19,9,15,25,31,42,43]
# even=0
# odd=0
# for i in elements:
#   if i%2==0:
#     even+=i
#   if i%2!=0:
#     odd+=i
# print(even,'this is the sum of the present elements')
# print(odd,'this is the sum of the present elements')
# ###################################################################################

# elements=[23,14,56,12,19,9,15,31,42,34]
# even=0
# everage=0
# odd=0
# odden=0
# for i in elements:
#   if i % 2 == 0:
#     even=even+i
#     everage+=1
#   if i % 2 != 0:
#     odd=odd+i
#     odden+=1
# m=even/everage
# n=odd%odden
# print(m)
# print(n)

# ####################################################################################
# x=0
# y=1
# z=0
# for x in range(0,100):
#   print(z,end=",")
#   x=y
#   y=z
#   z=x+y
# ###################################################################################
# user=int(input("enter the number:-- "))
# x=1
# y=1
# z=0
# a=0
# while True:
#   a+=1
#   x=y
#   y=z
#   z=x+y
#   if a==user:
#     print(z)
#     break
########################################################################################

# x=0
# y=1
# z=0
# count=0
# a=0
# user1=int(input("enter the first number:--  "))
# user2=int(input("enter the sicond number:--  "))
# while True:
#   count+=1
#   x=y
#   y=z
#   z=x+y
#   if z%user1==0:
#     a+=1
#   if a==user2:
#     break
# print(count)






##########################progress tracking###########################################
# x=0
# y=1
# z=0
# for x in range(0,10):
#     print(z)
#     x=y
#     y=z
#     z=x+y

# x=0
# y=1
# z=0
# count=0
# a=0
# user1=int(input("enter the first numbers:--  "))
# user2=int(input("enter the second numbers:--  "))
# while True:
#     # print(i)
#     count+=1
#     x=y
#     y=z
#     z=x+y
#     if z%user1==0:
#       a+=1
#     if a==user2:
#       break
# print(count)
#######################################
# user=int(input("enter the number:--  "))
# x=0
# y=1
# z=0
# while z<user:
#   x=y
#   y=z
#   z=x+y
# if z==user:
#   print(yes"fibonachi number")
# else:
#   print(no"fibonachi number")
#################################20-10-2021############################################

# user=int(input("Enter the number:--  "))

# for i in range(user):
#     b=1
#     be=[]import random,time
#     for r  in range(1,user-i):
#         print(end=" ")
#     for a in range(i+1):
#         be.append(b)
#         b=int(b*(i-a)/(a+1))
#     print(be)
##########################################################################################

##################### Name print ##########################################################
# a=["pratik","satish","tikaram","Munna","roshan","akash"]
# w=[]
# for z in range(len(a)):
#     for s in a:
#         print("\x1b[31m",s)
#     b=int(input("enter your number :"))
#     c=a.pop(b)
#     w.append(c)
#     for v in w:
#         print("\x1b[32m",v)
# #############################################################################################

#################################################################################

# a = "my name is vishal majumndar"
# s=0
# for i in a:
#     if i ==" ":
#         continue
#     s+=1
# print(s)
#######################################################################################

a=[1,1,1,2,2,3,3,4,4]
count=0
for i in a:
    count+=1
    a.append(count)
print(a)






