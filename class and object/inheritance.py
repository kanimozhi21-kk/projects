
class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class student(person):
    pass
x=student("mahesh","siva")
x.printname()


class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class student(person):
     def __init__(self,fname,lname):
        super().__init__(fname,lname)
        person.__init__(self,fname,lname)
        self.graduationyear=2024
x=student("kani","mozhi")
print(x.graduationyear)
x.printname()
             
