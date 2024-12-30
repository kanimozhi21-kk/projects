'''class employee:
    def __init__(self,name,id,salary,project):
        self.name=name
        self.id=id
        self.salary=salary
        self.project=project
    def show_sal(self):
        print("name:",self.name,"salary:",self.salary,"id:",self.id)
    def pro(self):
        print( self.project,"is working on")
emp=employee("kani",111,20000,"python")
emp.show_sal()
emp.pro()
'''

class students:
    def __init__(self,name,rank,points):
        self.name=name
        self.rank=rank
        self.points=points
    def gettername(self):
        print(self.name)
        print(self.rank)
    def settername(self,name,rank):
        self.name=name
        self.rank=rank
st1=students("kani",1,100)
st1.gettername()
st1.settername("3sha",2)
st1.gettername()

'''
class employee:
    def __init__(self,name,salary,id,project):
        self.name=name
        self.id=id
        self.salary=salary
        self.project=project
    def show_sal(self):
        print("name:",self.name,"salary:",self.salary,"id:",self.id)
    def value(self):
        print(self.name,"completed in project",self.project)

empy=employee("pavi",20000,126,"python")
empy.show_sal()
empy.value()'''
