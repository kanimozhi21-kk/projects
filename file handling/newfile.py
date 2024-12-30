open("newfile.txt","x")
f=open("newfile.txt","w")
f.write("something")
f=open("newfile.txt","a")
f.write("\nname\tpasssword")
f=open("newfile.txt","r")
a=f.read()
print(a)
a="name"
b="password"
f=open("newfile.txt","r")
lines=f.read().split("\n")
for x in lines:
       username=x.split("\t")
       if username[0]==a and username[0]==b:
              print("logged in")
       else:
            print("not logged")                    
 

