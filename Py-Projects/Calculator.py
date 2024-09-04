import math 
def add(a,b):
     return(a+b)
def sub (a,b):
     return(a-b)
def mul(a,b):
     return (a*b)
def div(a,b):
     return (a/b)


print("##########  Basic calculator #############")
Stop = True 
while Stop is not False:
    print("1)For additon \n2)For subraction\n 3) For MUltiplictaion\nFor Divide  ")
    user = int(input("Enter the number for opertaion :"))
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second  number: "))
    if user == 1:
         result=add(a,b)
         print( f"sum of the two numver are : {result}")
    elif user == 2:
         result=sub(a,b)
         print( f"subraction of the two numver are : {result}")
    elif user == 3:
         result=mul(a,b)
         print( f"multiplictaion  of the two numver are : {result}")
    elif user == 4:
         result=div(a,b)
         print( f"multiplictaion  of the two numver are : {result}")

    print("you want to continue ")
    choice=input("press y foor yes and n for no :").lower()
    if choice != "y":
         Stop=False
    print("thank for using it ")

         



