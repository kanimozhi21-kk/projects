file_name=input("enter a file:")
file_handler = open(file_name, "a")
if file_handler.writable():
    name=input("enter the name:")
    age=int(input("enter the age:"))
    place=input("enter a place:")
    
    if(age>=18):
        file_handler.write(f"name:{name}\n")
        file_handler.write(f"age:{age}\n")
        file_handler.write(f"place:{place}\n")
        file_handler.write("you are eligible\n")
        
        m1=int(input("enter a english mark:"))
        m2=int(input("enter a tamil mark:"))
        m3=int(input("enter a maths mark:"))
        m4=int(input("enter a cs mark:"))
        m5=int(input("enter a physics mark:"))
        m6=int(input("enter a chemistry mark:"))
        file_handler.write(f"english:{m1}\n")
        file_handler.write(f"tamil:{m2}\n")
        file_handler.write(f"maths:{m3}\n")
        file_handler.write(f"cs:{m4}\n")
        file_handler.write(f"physics:{m5}\n")
        file_handler.write(f"chemistry:{m6}\n")                               
        total=m1+m2+m3+m4+m5+m6
        avg=total/6
        print("enter a total:",total)
        print("enter the average:",avg)
        file_handler.write(f"total:{total}\n")
        file_handler.write(f"average:{avg}\n")
       
        if(avg>=90):
            print("you are eligible for Medical")
            file_handler.write("you are eligible for Medical")
        elif(avg>=80):
              print("you are eligible for engineer")
              file_handler.write("you are eligible for engineer")
        elif(avg>=70):
              print("you are eligible for computer science")
              file_handler.write("you are eligible for computer science")
        elif(avg>=60):
              print("you are eligible for polytehnic")
              file_handler.write("you are eligible for polytehnic")
        else:
            print("not eligible")
            file_handler.write("not eligible")
    else:
        print("data not managing")
        file_handler.write("data not managing")
else:
    print("file not writable")
    file_handler.write("file not writable")
file_handler.close()    
