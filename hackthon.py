# print("""my name is Roshan and i am 23 year old.i am form nagpur maharashtra.
# 	i have currentlly graduction. R.T.M.nagpur univrsity and i am ncc student and my best frinds chetan and my best teacther sonune sir in junior college.""")
# a=0
# p=0
# while a<1:
# 	print("""1)what is your name?
# 	1)amit
# 	2)roshan
# 	3)akash
# 	4)pradeep""")
# 	b=input("enter your choice:--  ")
# 	if b=="2":
# 		print("congratulation,your answer is right!!!!!")
# 		p+=1
# 	else:
# 		print("wrong answer")
# 	print("""2)how to old i am?
# 	1)20
# 	2)21
# 	3)22
# 	4)23""")
# 	c=input("enter your choice:--  ")
# 	if c=="4":
# 		print("congratulation,your answer is right!!!!!")
# 		p+=1
# 	else:
# 		print("wrong answer")
# 	print("""3)what is your loction?
# 	1)bhandra
# 	2)tumsar
# 	3)nagpur
# 	4)dharmashala""")
# 	d=input("enter your choice:--  ")
# 	if d=="3":
# 		print("congratulation,your answer is right!!!!!")
# 		p+=1
# 	else:
# 		print("wrong answer")
# 	print("""4)what is your qualifaction?
# 	1)12th
# 	2)graduction
# 	3)10th
# 	4)engineering""")
# 	e=input("enter your choice:--  ")
# 	if e=="2":
# 		print("congratulation,your answer is right!!!!!")
# 		p+=1
# 	else:
# 		print("wrong answer")
# 	print("""5)what is your univesity name?
# 	1)nagpur
# 	2)bhandra
# 	3)chandrapur
# 	4)himachal pradesh""")
# 	f=input("enter your choice:--  ")
# 	if f=="1":
# 		print("congratulation,your answer is right!!!!!")
# 		p+=1
# 	else:
# 		print("wrong answer")
# 	print("""6)what is your best friend name?
# 	1)akash
# 	2)chetan
# 	3)moreshwar
# 	4)pawan""")
# 	r=input("enter your choice:--  ")
# 	if r=="2":
# 		print("congratulation,your answer is right!!!!!")
# 		p+=1
# 	else:
# 		print("wrong answer")
# 	print("your answer",p)
############################################################################################################

##guessing game using random function
# import random
# for i in range(1,6):
#     rand = int(random.randint(1,10))
#     inp = int(input("enter number:"))
#     print(rand)
#     if inp == rand:
#         print("guessed")
#         break
#     else:
#         print("wrong guessed")
#         if rand < inp:
#             print("more")
#         else:
#             print("less")
# ########################################################################################

# die roller..
import random
print('welcome to dice rolling game: ')
s1=0
s2=0
for i in range(1,7):
    if i>1:
        f=input('roll again? (y/n)')   
        if f=='y':
            pass
        else:
            break
    p1=input('roll dice player 1: ')
    c=random.randint(1,6)
    # print(c)
    s1+=c
    p2=input('roll dice player 2: ')
    d=(random.randint(1,6))
    # print(d)
    s2+=d
print('player 1: ',s1,'\n','player 2: ',s2)
if s1>s2:
    print('player 1 is winner: congrats: ')
elif s2>s1:
    print('player 2 is winner: congrats: ')
else:
    print("it's a Tie: ")
##########################################################################################




