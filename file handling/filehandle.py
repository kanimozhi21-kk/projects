#open("new6.txt","x")
#f=open("new6.txt","w")
#f.write("age")
#f=open("new6.txt","a")
#f.write("\nname\tplace")
#f=open("new6.txt","r")
#a=f.read()
#print(a)

'''file=open ("good.txt","w")
l=["name\n","age\n"]
file.writelines(l)
file.close()'''
a="name"
b="place"
f=open("new6.txt","r")
lines=f.read().split("/n")
for x in lines:
     username=x.split("\t")
     if  username[0]==a and username[0]==b:
          print("successfully logged in")
          break
     else:
           print("not logged")

