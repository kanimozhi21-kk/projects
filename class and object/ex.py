'''class example_class():
    def method_1(self):
        print("Example Class method_1")
        
    def method_2(self,some_string):
        print("Example Class method_2 " + some_string)        

def main():
    # using class methods
    obj = example_class()
    obj.method_1()
    obj.method_2("I am passing some string")
    
    
if __name__ == "__main__": main()  


class Parent:
  def __init__(self, txt):
    self.message = txt

  def printmessage(self):
    print(self.message)

class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt)

x = Child("Hello, and welcome!")

x.printmessage()'''


class Employee:
    def __init__(self, name, salary):
       self.name=name
       self.salary=salary

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department=department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
        Manager = Manager("Alice", 90000, "IT")
Manager.display_info()







        
