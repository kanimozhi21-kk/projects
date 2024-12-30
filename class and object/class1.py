class newclass:
    n=7
    def __init__(self,name):
        self.name=name
        print("new")
    def prnt1(self):
        print(self.name)

obj=newclass("indhu")
print(obj.n)
obj.prnt1()
obj1=newclass("swathi")
print(obj1.n)
obj1.n=23
print(obj,obj1.n)



