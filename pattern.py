# # #####################question 15 A######################
# n=
#     for i in range(i):
#         print(' ',end='')
#     for k in range(i+1, row):
#         print(k,'',end='')
#     print('\n')
###########################################
# name="python.hub"
# print("I love"+name)
##########################################
# name = "Roshan"
# print("I love {}".format(name))
###########################################
# name = "Roshan"
# print(f"I love {name}")
###########################################
# ####Class Examples
# a=30
# b=20
# c=40
# print(a) if a>b else print(b)
# # if a>b:
#     print(a)
# else:
#   print(b)
# a=0
# while a<=10:
#     print("Nav")
#     a=a+1
################function question##################
# import calendar
# y=2020
# m=11
# y=int(input("enter year:--"))
# m=int(input("enter month:--"))
# print(calendar.month(y,m))
# ###################string question ###############################
# my_list =['a', 'b', 'c']
# my_str =''
# for word in my_list:
#     my_str = my_str+word
# print(my_str)
#######################################################
# my_tuple =['a', 'b', 'c']
# my_str =''
# for word in my_tuple:
#      my_str = my_str+word
# print(my_str)
######################################################
# my_set =['a', 'b', 'c']
# my_str =''
# for word in my_set:
#      my_str = my_str+word
# print(my_str)
#######################################################
# from array import*
# my_array = array ('u',['a', 'b', 'c'])
# my_str =''
# for word in my_array:
#      my_str = my_str+word
# print(my_str)
#####################################################
# my_string = 'copayassignment.com'
# for i in range(my_string):
#     print(i)
######################################################
# x=(i for i in range(3))
# for i in x:
#     print(i)
# ######################################################
# user=int(input("enter a value:--"))
# x=0
# y=1
# z=0
# for x in range(1,user+1):
#     print(z)
#     x=y
#     y=z
#     z=x+y
# ######################################################
# for a in range(10):
#     count=0
#     for i in range(1,a+1):
#         if a%i==0:
#             count+=1
#     if count==2:
#         print(a,end=' ')
# print()
#####################################################
# for i in range(1,11):
#     count=0
#     for j in range(1,i+1):
#         c=0
#         for k in range(1,j+1):
#             if j%k==0:
#                 c+=1
#         if c==2 or c==1:
#             print(j,end=",")
#     print()
####################################################
# a=int(input("enter your number :--"))
# b=a%1000
# c=a//1000
# w=b//100
# d=b%100
# print(str(c)+str(d)+str(w))
#####################happy number ########################
# for a in range(1,int(input("Enter Num:"))):
#     f = a
#     while True:
#         total = 0
#         while a>0:
#             b=a%10
#             a = a//10
#             total += b*b
#         a=total
#         if total == 1:
#             print(f)
#             break
#         if a == 4:
#             break
############################################### Extra Qs:

# a=int(input('Enter a No.: '))

# s=a%1000
# s2=s//100
# m=a-s
# b=((s%100)*10)+s2
# print(m+b)
#######################################################
# for i in range(1,11):
#     b=0
#     for j in range(1,11):  
#         print(i*j,end="| ")
#         b+=10
#     print()
##########################################################
# for i in range(7):
#     for j in range(5):
#         if ((i==0 or i==3 and (i!=0)and(j!=0)) or(j==4 or j==0)):
#              print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
####################################################
# for i in range(7):
#     for j in range(5):
#         print(j,end=" ")
#         if (((i==0 or i==4) and j==2)or (((i==1)or(i==3))and (j==1 or j==3))or(i==2 and(j==0 or j==4))):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# #######################################################
# user=int(input("enter the row:--"))
# for row in range(user):   
#     for col in range(user-row-1):
#         print(" ",end=" ")
#     for col in range(row,-1,-1):
#         print(user-col,end=" ")
#     print()
# #########################################################
# user=int(input("enter the rows:--"))
# i=1
# while (user>0):
#     b=1
#     while (b<i):
#         print(" ",end=" ")
#         b+=1
#     j=1
#     while (j<=(user*2)-1):
#         print("*",end=" ")
#         j+=1
#     print()
#     user-=1
#     i+=1
# ##########################################################
# user=int(input("ther the number:--"))
# for i in range(0,user):
#     for s in range(0,user-i-1):
#         print(end=" ")
#     for j in range(0,i+1):
#         if ((i>=2 and i<user-1) and (j>0 and j<i)):
#             print(end="  ")
#         else:
#             print("*",end=" ")
#     print()
# ############################################################
# a=int(input("enter number :"))
# for s in range(1,a+1):
#     for v in range(1,s+1):
#         print(v,end="")
#     print()
# ###############################################################
# user=int(input("enter the row:--"))
# i=1
# for row in range(1,user+1):
#     for col in range(1,row+1):
#         print(i,end="")
#         i+=1
#     print()
# #######################"B"#######################################
# for i in range(7):
#      for j in range(4):
#         # if i>3:
#         if((j==0 or j==3)and(i!=0 or i!=3 or i!=6))or(i==0 or i==3 or i==6):
#             print("*",end=" ")
#         else:
#             print(" ",end="  ")
#     print()
########################################################################7
# for i in range(n):
#     if i==0:
#         print("","*"*3," ")
#     elif i==1 or i==2 or i==4 or i==5 or i==6:
#         print("*"," "*1,"*")
#     elif i==3:
#         print("*"*5)

# for row in range(7):
#     for col in range(5):
#         if (col==0 or col==4) or (row==0 or row==3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ") 
#     print()

# for row in range(7):
#     for col in range(5):
#         if row in (0,1,2,3,4,5,6) and col in (0,4):
#             print("*",end=" ")
#         elif row==0 and col in (1,2,3):
#             print("*",end=" ")
#         elif row==3 and col in (1,2,3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# #####################question 16 B######################
# for row in range(7):
#     for col in range(5):
#         if row in (1,2,4,5) and col in (0,4):
#             print("*",end=" ")
#         elif row in (0,6) and col ==0:
#             print("*",end=" ")  
#         elif row==3 and col==0:
#             print("*",end=" ")
#         elif row in (0,3,6) and col in (1,2,3):
#             print("*",end=" ")
#         elif row in (1,2) and col==4:
#             print("*",end=" ")
#         elif row in (4,5) and col==4:
#             print("*",end=" ")       
#         else:
#             print(" ",end=" ")    
#     print()
###################question 17 C######################
# for row in range(7):
#     for col in range(5):
#         if row in (1,2,3,4,5) and col==0:
#             print("*",end=" ")
#         elif row==0 and col in (1,2,3):
#             print("*",end=" ")
#         elif row==6 and col in (1,2,3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()        
# #################question 18 D#######################
# for row in range (7):
#     for col in range(5):
#         if row in (1,2,3,4,5) and col in (0,4):
#             print("*",end=" ")
#         elif row ==0 and col in (0,1,2,3):
#             print("*",end=" ")
#         elif row ==6 and col in (0,1,2,3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()        
###############question 19 E##########################

# for row in range(7):
#     for col in range(5):
#         if row in (0,1,2,3,4,5) and col==0:
#             print("*",end=" ")
#         elif row in (0,6) and col in (0,1,2,3):
#             print("*",end=" ")
#         elif row ==3 and col in (1,2):
#             print("*",end=" ")    
#     print( ) 
###########question 20 F ########################
# for row in range(7):
#     for col in range(5):
#         if row in (0,1,2,3,4,5,6) and col==0:
#             print("*",end=" ")
#         elif row ==0 and col in (0,1,2,3,4):
#             print("*",end=" ")
#         elif row ==3:
#              print("*",end=" ")           
#     print()
############question 21 G #######################
# for row in range(7):
#     for col in range(4):
#         if row in (0,1,2,3,4,5,6) and col==0:
#             print("*",end=" ")
#         elif row in (0,6) and col in (1,2,3):
#             print("*",end=" ")
#         elif row==1 and col==3:
#             print("*",end=" ")
#         elif row in (4,5) and col==3:
#             print("*",end=" ")
#         elif row==3 and col in (2,3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()    

# for row in range(7):
#     for col in range(4):
#         if row in (1,2,3,4,5) and col==0:
#             print("*",end=" ")
#         elif row in (0,6) and col in (1,2):
#             print("*",end=" ")
#         elif row==1 and col==3:
#             print("*",end=" ")
#         elif row in (4,5) and col==3:
#             print("*",end=" ")
#         elif row==3 and col in (2,3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# #################question 22 H #######################
# for row in range (7):
#     for col in range (5):
#         if row in (0,1,2,3,4,5,6) and col in(0,4):
#             print("*",end=" ")
#         elif row ==3 and col in (1,2,3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
####################question 23 I####################
# for row in range(7):
#     for col in range(7):
#         if row==0 and col in (0,1,2,3,4,5,6,7):
#             print("*",end=" ")
#         elif row in (1,2,3,4,5) and col==3:
#             print("*",end=" ")
#         elif row==6 and col in (0,1,2,3,4,5,6,7):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# ###############question 24 J#######################
# for row in range(7):
#     for col in range(5):
#         if row==0 and col in (0,1,2,3,4,5,6,7):
#             print("*",end=" ")
#         elif row in (0,1,2,3,4,5,6,7) and col==3:
#             print("*",end=" ")
#         elif row==5 and col==1:
#             print("*",end=" ")
#         elif row==6 and col in (1,2):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# ################question 25 K ####################
# for row in range (7):
#     for col in range(5):
#         if row in (0,1,2,3,4,5,6,7) and col==0:
#             print("*",end=" ")
#         elif row==0 and col==3:
#             print("*",end=" ")
#         elif row==1 and col==2:
#             print("*",end=" ")
#         elif row==2 and col==1:
#             print("*",end=" ")
#         elif row==4 and col==1:
#             print("*",end=" ")
#         elif row==5 and col==2:
#             print("*",end=" ")
#         elif row==6 and col==3:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print() 
# ########################question 26 L ################
# for row in range(7):
#     for col in range(5):
#         if row in (0,1,2,3,4,5,6) and col==0:
#             print("*",end=" ")
#         elif row==6 and col in (1,2,3,4):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print() 
# #################question 27 M ########################  
# for row in range (7):
#     for col in range(6):
#         if row in (0,1,2,3,4,5,6) and col in (0,4):
#             print("*",end=" ")
#         elif row==1 and col in (1,3):
#             print("*",end=" ")
#         elif row==2 and col in (2,2):
#             print("*",end=" ")
#         elif row==3 and col==2:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
##################question 28 N ##########################
# for row in range(7):
#     for col in range(5):
#         if row in (0,1,2,3,4,5,6) and col in (0,4):
#             print("*",end=" ")
#         elif row==1 and col==1:
#             print("*",end=" ")
#         elif row==2 and col==2:
#             print("*",end=" ")
#         elif row==3 and col==3:
#             print("*",end=" ")
#         elif row==4 and col==4:
#             print("*",end=" ")
#         elif row==5 and col==5:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#################question 29 O ###########################
# for row in range(7):
#     for col in range(5):
#         if row in (1,2,3,4,5) and col in (0,4):
#             print("*",end=" ")
#         elif row==0 and col in (1,2,3):
#             print("*",end=" ")
#         elif row==6 and col in (1,2,3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# #############question 30 P #############################
# for row in range (7):
#     for col in range(5):
#         if row in (0,1,2,3,4,5) and col==0:
#             print("*",end=" ")
#         elif row==0 and col in (1,2,3):
#             print("*",end=" ")
#         elif row==3 and col in (1,2,3):
#             print("*",end=" ")
#         elif row==1 and col==4:
#             print("*",end=" ")
#         elif row==2 and col==4:
#             print("*",end=" ") 
#         else:
#             print(" ",end=" ")
#     print()
# ###################question 31 Q ########################     
# for row in range (8):
#     for col in range(5):
#         if row in (1,2,3,4,5) and col in (0,4):
#             print("*",end=" ")
#         elif row==0 and col in (1,2,3):
#             print("*",end=" ")
#         elif row==6 and col in (1,2,3):
#             print("*",end=" ")
#         elif row==5 and col==3:
#             print("*",end=" ")
#         elif row==7 and col==3:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# ###################question 32 R #########################
# for row in range(8):
#     for col in range(5):
#         if row in (0,1,2,3,4,5,6) and col==0:
#             print("*",end=" ")
#         elif row==0 and col in (1,2,3):
#             print("*",end=" ")
#         elif row==1 and col==4:
#             print("*",end=" ")
#         elif row==2 and col==4:
#             print("*",end=" ")
#         elif row==3 and col in (1,2,3):
#             print("*",end=" ")
#         elif row==4 and col==2:
#             print("*",end=" ")
#         elif row==5 and col==3:
#             print("*",end=" ")
#         elif row==6 and col==4:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# #####################question 33 S ########################
# for row in range(7):
#     for col in range (5):
#         if row==0 and  col in (1,2,3,4):
#             print("*",end=" ")
#         elif row==3 and col in (1,2,3):
#             print("*",end=" ")
#         elif row==6 and col in (0,1,2,3):
#             print("*",end=" ")
#         elif row in (1,2) and col==0:
#             print("*",end=" ")
#         elif row in (4,5) and col==4:
#             print("*",end=" ")
#         else:
#             print("*",end=" ")    
#     print()
# #######################question 34 T ########################
# for row in range (7):
#     for col in range(7):
#         if row==0 and col in (0,1,2,3,4,5,6,7):
#             print("*",end=" ")
#         elif row in (0,1,2,3,4,5,6) and col==3:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# ###################question 35 U ##############################
# for row in range(7):
#     for col in range(5):
#         if row in (0,1,2,3,4,5) and col==0:
#             print("*",end=" ")
#         elif row in (0,1,2,3,4,5) and col==4:
#             print("*",end=" ")
#         elif row==6 and col in (1,2,3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# #################question 36 V ################################
# for row in range(4):
#     for col in range(7):
#         if row==1 and col in (0,4):
#             print("*",end=" ")
#         elif row==2 and col in (1,3):
#             print("*",end=" ")
#         elif row==3 and col==2:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# ##################question 37 W ################################
# for row in range (7):
#     for col in range(7):
#         if row in (0,1,2) and col in (0,6):
#             print("*",end=" ")
#         elif row==3 and col in (0,3,6):
#             print("*",end=" ")
#         elif row==4 and col in (0,2,4,6):
#             print("*",end=" ")
#         elif row==5 and col in (0,1,5,6):
#             print("*",end=" ")
#         elif row==6 and col in (0,6):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#################question 38 X ##################################
# for row in range (7):
#     for col in range (5):
#         if row in (0,1,5,6) and col in (0,4):
#             print("*",end="")
#         elif row in (2,4) and col in(1,3):
#             print("*",end=" ")
#         elif row==3 and col==2:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#################question 39 Y##################################
# for row  in range (7):
#     for col in range (7):
#         if row==0 and col in (0,6):
#             print("*",end=" ")
#         elif row==1 and col in (1,5):
#             print("*",end=" ")
#         elif row==2 and col in (2,4):
#             print("*",end=" ")
#         elif row==3 and col==3:
#             print("*",end=" ")
#         elif row in (4,5,6) and col==3:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()        


###################question Z 40 ###################################
# for row in range(7):
#     for col in range(5):
#         if row==0 and col in (0,1,2,3,4,5,6):
#             print("*",end=" ")
#         elif row==1 and col==4:
#             print("*",end=" ")
#         elif row==2 and col==3:
#             print("*",end=" ")
#         elif row==3 and col==2:
#             print("*",end=" ")
#         elif row==4 and col==1:
#             print("*",end=" ")
#         elif row==5 and col==0:
#             print("*",end=" ")
#         elif row==6 and col in (0,1,2,3,4,5):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
####################stop##################################
# for row in range (6):
#     for col in range (7):
#         if (row==0 and col %3!=0) or (row==1 and col%3==0) or (row-col ==2) or (row +col==8):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
###################hard pattern##############################
# for row in range (6):
#     for col in range (7):
#         if row ==0 and col in (1,2,4,5):
#             print("*",end=" ")
#         elif row==1 and col in(0,3,6):
#             print("*",end=" ")
#         elif row==2 and col in (0,6):
#             print("*",end=" ")
#         elif row ==3 and col in(1,5):
#             print("*",end=" ")
#         elif row==4 and col in (2,4):
#             print("*",end=" ")
#         elif row==5 and col==3:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
##############harshad number#############################
# user=int(input("enter harshad number:--"))
# a=user
# sum=0
# while user<a:
#     sum=sum+(a%10)
#     a=a//10 
# if (user!=sum==0):
#     print(user,"is harshad number")
# else:
#     print(user,"is not a harshad number")

# sum=0
# user=int(input("enter the number:--"))
# n=user
# while n > 0:
#     r=n%10
#     sum=sum+r
#     n=n//10
# if (%sum==0):
#     print(user,"is harshad number")
# else:
#     print(user,"is not a harshad number")



# user=int(input("enter a armstrong number:--"))
# sum=0
# a=user
# s=0
# while a >0:
#     a=a//10 
#     s+=1
# a=user
# while a >0:
#     digit=a%10
#     sum+=(digit**s)
#     a//=10
# if sum==user:
#     print(user,"is a armstrong numer")
# else:
#     print(user,"is not a armstrong numer")

# user=int(input("enter the number:--"))
# sum=0
# a=user
# s=0
# while a>0:
#     a=a//10
#     d=a%10
#     sum+=d**s
#     a//10
# if sum==user:
#     print(user,"is a armstrong number")
# else:
#     print(user,"is not a armstrong number")
 
#########second number find########################
# user=int(input("enter the number:--"))
# a=user % 1000
# b=a//100
# if b%2==0:
#     print("yes is a third number",b)
# else:
#     print("no")


# user=int(input("enter the number:--"))
# a=user % 1000
# b=a//10
# if b%2==0:
#     print("yes is a third",b)
#     c=user*10+b
#     print(c)
# else:
#     c=user*10+b
#     print(c)
#############################################
# user=int(input("enter the number:--"))
# a=user%10000
# e=a//10000
# # print(e)
# b=a//1000
# c=b%100
# print(str(e)+str(c)+str(b))
# #############################################
# user=int(input("enter the number:--"))
# for i in range(1,user+1):
#     print(str(i)*i)
##############################################
# a=int(input())
# b=int(input())
# print(a+b)
##############################################
# a="hello world"
# b=len(a)
# c=len(a)//2
# d=a[:c]
# e=a[c:]
# print(d)
# print(e)
##############################################
# for i in range(1,6):
#     print("*"*i)
##############################################
# i=input()
# for i in i:
#     print(i,end="")
# print()
#############################################
# i=input()
# a=i.replace("",",")
# print(a.strip(","))
############################################
# row = 6
# for i in range (0,row):
#     for j in range(row -1, i,-1):
#         print(j,'',end='')
