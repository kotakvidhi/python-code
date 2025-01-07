import random
x=random.randint(1,20)
print("No=",x)
a=int(input("Enter square =>"))
if a == x*x*x:
    print("right")
else:
    print("wrong")
