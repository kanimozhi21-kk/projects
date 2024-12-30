'''def add(x,y):
      return x+y
def sub(x,y):
      return x-y
def multi(x,y):
      return x*y
def divide(x,y):
      if y!=0:
        return x/y
      else:
            return "division by zero error!"
choice=input("choose operation(+,-,*,/):")
num1=float(input("enter first number:"))
num2=float(input("enter second number:"))
if choice=='+':
   print(f"result:{add(num1,num2)}")
elif choice=='-':
         print(f"result:{sub(num1,num2)}")
elif choice=='*':
         print(f"result:{multi(num1,num2)}")
elif choice=='/':
      print(f"result:{divide(num1,num2)}")
else:
      print("invalid operation")


sentence=input("enter a sentence:")
words=sentence.split()
reversed_sentence=" ".join(reversed(words))
print(f"reversed sentence:{reversed_sentence}")      
'''

key=list(str(input(f"please enter a key for value{x+1}:")))
if x==0:
   else str(input(f"\nplease enter a key for value{x+1}:"))
for x in range(3)
     value=list(str(input(f"\nplease enter a bool for value{x+1}:")))
for x in range(3)
     boolvalues=dict(zip(key,value))
       