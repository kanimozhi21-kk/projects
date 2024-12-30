'''def value():
    n=1
    while n<10:
        val=n*n
        yield val
        n+=2
a=value()
for i in a:
    print(i)

def func(x):
    x("just a print")
func(print)
func(input)'''

def fib(limit):
    a,b=0,1
    while b<limit:
        yield b
        a,b=b,a+b
x=fib(200)

for i in x:
    print(i)

        
