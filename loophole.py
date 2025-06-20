from pexpect.replwrap import python  #for loop=used to iterate through a sequence:list,tuple or a string
 #looping through a range
for  x in range(10):
    print(x)
    #loop through range=10-15
    for y in range(10,15):
        print(y)
#loop through a string
for z in "hello":
    print(z)
#loop through a list
fruits=["apple","banana","tangerine","guava"]
for a in fruits:
    print(a)
#breakstatements can be used to terminate a loop
users=["peter","james","john"]
for user in users:
    print(user)
    if user=="john":
        break
#print1..10 using for loop
for r in range(1,11):
    print(r)
#print python programming S times using for loop
for x in range(7):
    print("python programming")
#PRINT EVEN NUMBERS FROM 2 TO 20.USE range(start,stop,step)
for e in range(3,27,5):
    print(e)