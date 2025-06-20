#conditional statements
"""if statement
 evaluates a condition and execute a block of code if the condition is true
if condition:
                block of code to be executed if condition is true"""
x=3
if x<5:
    print(x,"is less than 5")

#if . . else
"""if condition:
            block of code to be executed if condition is true
            else:
            block of code to be executed if condition is false"""
age=22
if age>=18:
    print("you are eligible to vote")
else:
    print("not eligible to vote")
    #write a program that asks the user for their age 
    #and check if they are eligible to drive. tip;vote age>=18
user_age=int(input("enter your age"))
print("my age is",user_age)
if user_age>=18:
 print("you are eligible to drive")
if user_age<18:
 print("you are not eligible to drive")

else:
 print("you are not eligible to vote")
 #get user age and check if they are eligible to drive
 user_age=int(input("enter your age"))
 if user_age>=18:
  print("you are eligible to drive")
  #program that asks user for a number if
  #the number is even or odd
  num=int(input("enter a number to check if even or odd"))
  if num%2==0:
   print("the number is even")
  else:
   print("the number is odd")