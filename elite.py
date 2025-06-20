#elif=used to another condition to test if the condition is true
#if condition is false
"""if . .elif. .else
if condition:
    block of code to be executed if condition is true
    elif condition:
    block of code to be
else:"""
a=5
if a>12:
    print("a is greater than 12")
elif a<5:
    print("a is less than 5")
elif a==5:
    print("a is equal to 5")
else:
        print("a is not equal to 5")
#a program that prompts user for age then it checks
#18-25-young adult
#25-40 adult
#40>-mature adult
#<18-child
age=int(input("enter your age"))
if 18 <= age < 25:
 print("you are a young adult")
 if 25 <= age < 40:
  print("you are an adult")
elif 40 <= age < 100:
 print("you are a mature adult")
if age<18:
 print("you are a child ")
#a program that asks for marks prints students grade
#80-100=A
#70-80=B
#60-70=C
#50-60=D
#<=FAIL
marks= int(input("enter your marks"))
if marks >= 80 and marks <= 100:
 print("your grade is A")
elif marks >= 70 and marks < 80:
 print("your grade is B")
elif marks >= 60 and marks < 70:
 print("your grade is C")
elif marks >= 50 and marks < 60:
 print("your grade is D")

if marks<50:
 print("your grade is FAIL")
else:
    print("enter a valid number between 1 and 100")
#a program that prompts users for two numbers then prints
#the larger or if they are equal
num1=int(input("enter first number"))
num2=int(input("enter second number"))
if num1>num2:
 print(num1,"is greater than",num2)
elif num1==num2:
 print(num1,"is equal to",num2)
else:
 print(num2,"is greater than",num1)


