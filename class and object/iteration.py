names=("kani","mozhi","madhu")
value=iter(names)
print(next(value))
print(next(value))

mystr="loop"
l=iter(mystr)
print(next(l))
print(next(l))
print(next(l))


mytuple=("comp","key","mouse")
for i in mytuple:
    print(i)
