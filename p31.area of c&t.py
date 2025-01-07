print("press 1 for circle")
print("press 2 for triangle")
op=int(input("Enter opt =>"))
if op==1:
    r=float(input("Enter radius =>"))
    print("Area of the circle",r*r*3.14)
elif op==2:
    h=float(input("Enter height =>"))
    b=float(input("Enter base =>"))
    print("base of the triangle",h*b*0.5)
else:
    print("wrong opt")