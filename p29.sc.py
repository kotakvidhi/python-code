print("press 1 for square")
print("press 2 for cube")
op=int(input("Enter opt =>"))
if op==1:
    no=int(input("Enter any number =>"))
    print("square",no*no)
elif op==2:
    no=int(input("Enter any number =>"))
    print("cube",no*no*no)
else:
    print("wrong op")