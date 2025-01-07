import random
x=random.randint(1,20)
y=random.randint(1,20)
print("No1=",x)
print("No2=",y)
a=int(input("Enter add =>"))
if a == x+y:
    print("right")
else:
    print("wrong")

