'''from abc import ABC

class bank(ABC):
    def bank_info(self):
        print("welcome to bank")
    def interest(self):
        pass

class SBI(bank):
    def interest(self):
        print("hii")
    def balance(self):
        print("balance in 100")

s=SBI()
s.bank_info()
s.balance()
s.interest()


from abc import ABC
class bank(ABC):
    def bank_info(self):
        print("welcome to bank")
   
    def interest(self):
        "abstractmethod"
        pass
       

class SBI(bank):
    def balance(self):
        print("balance in 100")

class sub1(SBI):
    def interest(self):
        print("in SBI bank interest in 4 rupees")

s=sub1()
s.bank_info()
s.balance()
s.interest()'''


from abc import ABC, abstractmethod

class car(ABC):
    @abstractmethod
    def moving_backward(self):
        pass
    @abstractmethod
    def moving_forward(self):
        pass
    @abstractmethod
    def fm(self):
        pass

class toyota(car):
    def moving_backward(self):
        print("the car moving backward")
    
    def moving_forward(self):
        print("the car moving forward")
    def fm(self):
        print("the car fm is playing")


class audi(toyota):
    def moving_backward(self):
        print("the car moving backward")
    def moving_forward(self):
        print("the car moving forward")
    def fm(self):
        print("the car fm is playing")

        

s=audi()
s.moving_forward()

s.fm()
s.moving_backward()






