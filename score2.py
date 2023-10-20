name= input("Enter your first name: ")
family=input("Enter your family name: ")
a=int(input("Enter first score:" ))
b=int(input("Enter second score:"))
c=int(input("Enter third score:"))
average=(a+b+c)/3

if average>17:
    print("great")
if 12<average<17:
    print("normal")
if average<12:
    print("fail")