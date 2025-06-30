#function with statement
#def function name(parameters)
#return
from xlrd.formula import num2strg


def myfunction(g):
    return g*7
#calling the function
result=myfunction(10)#store the returned value in a variable
print(result)
#way 2
print(myfunction(40))
print(myfunction(70))
#function that adds two numbers and returns the sum
def addtwonumbers(num1,num2):
 sum=num1+num2
 return sum
#calling the function
print(addtwonumbers(10,20))
print(addtwonumbers(30,40))
mysum=addtwonumbers(50,30)
print(mysum)
#function that finds maximum of three numbers hint max(num1,num2,num3)
def maxnum(p,q,r):
    return max(p,q,r)
#calling the function
print(maxnum(10,20,40))
#function that determines even or odd number(num%==0)
#prompts user for two numbers from user input, then create function
#that multiplies the numbers
input1=int(input("enter first number"))
input2=int(input("enter second number"))
#function that multiplies two numbers
def multiplytwonumbers(m,n):
    return m*n
#calling the function and store the returned value in variable results
results=multiplytwonumbers(input1,input2)
print(multiplytwonumbers(input1,input2))
#function that determines even or odd number(num%2==0)
 #calling the function
def evenodd(x):
    if x%2==0:
        print(x,"is even number")
    else:
        print(x,"is odd number")
evenodd(10)
evenodd(11)
evenodd(24)
#function to find largest of three numbers
def largestnum(x,y,z):
    return (x,y,z)
#prompts user for three numbers from user input then creates function
num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))
#calling the function
print(largestnum(num1,num2,num3))



