def reverse(num):
    rev=0
    while(num>0):
        rev=rev*10+num%10
        num=num//10
    return rev
def fact(num):
    if(num==0 or num==1):
        return 1
    else:
        return num*fact(num-1)
def fibbo(n):
    n1, n2 = 0, 1
    print("Fibonacci Series:", n1, n2,end=" ")
    for i in range(2, n):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3,end=" ")


def palindrome(num):
    a=reverse(num)
    if(a==num):
        return "Palindrome"
    else:
        return "Not a Palindrome"
def armst(num):
   
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
       return num,"an Armstrong number"
    else:
       return num,"not an Armstrong number"

def myfun(ch):
    if(ch==1):
        num=int(input("Enter the number to reverse:"))
        print(reverse(num))
    elif(ch==2):
           num=int(input("Enter the number to find factorial:"))
           print(fact(num))
    elif(ch==3):
        num=int(input("Enter the number to find palindrome or not:"))
        print(palindrome(num))
    elif(ch==4):
        n=int(input("Enter the number to find fibbonacci series:"))
        print(fibbo(n))
    elif(ch==5):
          num=int(input("Enter the number to find Armstrong or not:"))
          print(armst(num))

       
for i in range(1,4):

    ch=int(input("Enter your choice 1/2/3/4/5:"))
    myfun(ch)
    