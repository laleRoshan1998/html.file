# a=["roshan","akash","satish","raj"]
# for i in range (len(a)):
#     a.pop(0)
# print(a)


#############odd and even number ######################

# a=[1,2,3,4,5,6,7,8,9]
# b=[]
# c=[]
# for i in range(len(a)):
#     if a[i]%2==0:
#         b=a.pop(i)
#         a.append(b)
# print(a)
#########################################################

# a=[100,51,6,33,55,777,90,99,22,1,3,2,5,77,88,00,44,333,56,666,]
# c=a.copy()
# print(c)
# l=[]
# for j in range(len(a)):
#     b=0
#     for i in c:
#         if i>b:
#             b=i
#     # print(b)
#     l.append(b)
#     # print(l)
#     c.remove(b)
#     # print(c)
# print(l)
# for i in l:
#     print(i)
#     l.append(1)
####################assending and disending order####################

# a=[100,51,6,33,55,77,90,99,22,1,3,2,5,88,44,33,56,66,]
# for i in range(len(a)-1):
#     for j in range(len(a)-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)
##################################################################

# a=[100,51,6,33,55,77,90,99,22,1,3,2,5,88,44,33,56,66,]
# for i in range(len(a)-1):
#     for j in range(len(a)-1):
#         if a[j]<a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)
################################################################

# a=[1,2,3,4,5,6,7,8,9,10]
# b=[5,6,7,8,9,10,11,12,13,14,15]
# c=a+b
# d=[]
# for i in c:
#     if i in a and i not in b:
#         d.append(i)
#     if i in b and i not in a:
#         d.append(i)
# print(d)
#########################################################

# a=[1,1,1,2,2,3,3,4,4]
# b=0
# count=0
# while count<len(a):
#     for i in a:
#         if a[count]==i:
#             if b==i:
#                 a.remove(a[count+1])
#             b+=1
#     count+=1
#     b+=1
# print(count)

# a=[1,1,1,2,2,3,3,3,4,4,4,4]
# for i in a:
#     if i in a and a.count(i)!=1:
#         a.remove(i)
#         if a.count(i)>1:
#             a.remove(i)
# a.sort()
# print(a)



# user=int(input("enter number"))
# user2=int(input("enter second number"))
# user3=int(input("enter threed number"))
# a=0
# for i in range(user3):
#     if i==user2:
#         a+=1
#     if user2==user:
#         a+=1
#     if user3==user:
#         a+=1
#     if user==user2:
#         a+=1
# print(a)

