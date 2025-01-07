print("press 1 for max2")
print("press 2 for max3")
op=int(input("Enter opt =>"))
if op==1:
    no1=int(input("Enter no1 =>"))
    no2 = int(input("Enter no2 =>"))
    if no1>no2:
        print("no1 is greater")
    else:
        print("no2 is greater")
elif op==2:
    no1 = int(input("Enter no1 =>"))
    no2 = int(input("Enter no2 =>"))
    no3 = int(input("Enter no3 =>"))
    if no1>no2:
        print("no1 is greater")
    elif no2>no3:
        print("no2 is greater")
    else:
        print("no3 is greater")
else:
    print("wrong opt")