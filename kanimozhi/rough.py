'''n=5
for i in range(0,n):
     for x in range(0,n-12):
          print(' ',end=" ")
          for x in range(0,n+1):
               print("*",end=" ")
               print()

 num =11
if num < 0:
   print("Enter a positive number")
else:
      sum = 0
      while(num > 0):
         sum += num
         num -= 1
         print("The sum is", sum)               

year=int(input("enter a year:"))
if (year%4==0 and year%100!=0)or(year%400==0):
   print(f"{year}is a leap year")
else:
      print(f"{year}is not leap year")

import math
radius=float(input("enter the radius of circle:")) 
area=math.pi*radius**2
print(f"area of the circle:{area}") 


s=input("enter a string:")
vowels="aeiouAEIOU"
count=sum(1 for char in s if char in vowels)
print(f"number of vowels:{count}")

num=int(input("enter a number:"))
for i in range(1,11):
     print(f"{num}x{i}={num*i}")

num=int(input("enter a number:"))
if num>1:
   for i in range(2,num):
        if num%i==0:
           print(f"{num}is not prime")
           break
        else:
              print(f"{num}is prime")
else:
        print(f"{num}is not prime")


n=float(input("enter a intrest:"))
r=float(input("enter a amount:"))
t=float(input("enter a year:"))
p=float(input("enter a com:"))
comound=n*(1+r)/(p*100)**(p*t)
print(f"{comound}")
'''
import math
n=int(input("enter the 'n' value:"))
prime=(n+1)*[True]
prime[0]=prime[1]=False
m=int(math.sqrt(n))
for i in range(2,m+1):
     for j in range(2*i,n+1,i):
          prime[j]=False
print("the list of prime num upto",n)
for i in range(n+1):
     if prime[i]:
        print(i,sep=",",end=" ")
        print()
        print("the list if non_prime numbers upto",n)
for i in range(n+1):
     if not prime[i]:
        print(i,sep=",",end=" ")