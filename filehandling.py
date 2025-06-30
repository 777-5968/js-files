#file handling
#open(filename,mode)
#modes=r-read,w-write,a-append,c-create
#write
j=(open("test.txt","w"))
j.write("hello world \n")
j.close()
#append
j=(open("myfile.txt","a"))
j.write("hello python students")
j.close()
#read
j=(open("test.txt","r"))
print(j.read())
j.close()
#create
j=(open("myproj.txt","x"))
j.write("hello python students")
j.close()
#create a file demo.txt
#write some data into it
#read the contents
#append some data
#create
y=(open("code.txt","x"))
y.write("hello python students")
y.close()
#read
j=(open("demo.txt","r"))
print(j.read())
j.close()
#append
j=(open("demo.txt","a"))
j.write("hello python students")
j.close()
#write
j=(open("demo.txt","w"))
j.write("hello world \n")
j.close()


