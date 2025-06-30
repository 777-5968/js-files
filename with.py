#with statement
with open("myproj.txt","w") as z:
    z.write("python \n")
    z.write("writing files in python \n")
    z.write("writing")
    #append
    with open("myproj.txt","a") as x:
     x.write("hello python students\n")
    #read the contents of the file
    with open("myproj.txt","r") as y:
        print(y.read())