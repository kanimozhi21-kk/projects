class cl:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("this is a function")
    def func(self):
        print(self.name,self.age)
c=cl("kani",21)
c.func()

class employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        print("salary in increase in monthly")
    def read(self):
        print(self.name,self.age,self.salary)
    def __str__(self):
        return str(self.name)
obj=employee("kani",21,20000)
obj.read()
print(obj)


'''class add:
    def __init__(self,f,s):
        self.first_no=f
        self.second_no=s
        
    def tot(self):
        print("first number:",self.first_no)
        print("second number:",self.second_no)
        total=self.first_no+self.second_no
        print("the total value:",total)
sum=add(34,4)
sum2=add(43,5)
sum.tot()
sum2.tot()'''
