a=int(input("Enter no1 =>"))
b=int(input("Enter no2 =>"))
c=int(input("Enter no3 =>"))

if a>b and a>c:
    print("no1 is greater")
elif b>c and b>a:
    print("no2 is greater")
elif c>a and c>b:
    print("no3 is greater")
else:
    print("All are equal")