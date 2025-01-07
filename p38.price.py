print("press 1 for pizza")
print("press 2 for burger")
print("press 3 for sandwich")
print("press 4 for dosa")
print("press 5 for vada pav")
op=int(input("Enter opt =>"))
if op==1:
    print("300 rs pizza")
    qty = int(input("Enter qty =>"))
    print("Bill of pizza = ", qty * 300)
elif op==2:
    print("200 rs burger")
    qty = int(input("Enter qty =>"))
    print("Bill of burger = ", qty * 200)
elif op==3:
    print("120 rs sandwich")
    qty = int(input("Enter qty =>"))
    print("Bill of sandwich = ", qty * 120)
elif op==4:
    print("100 rs dosa")
    qty = int(input("Enter qty =>"))
    print("Bill of dosa = ", qty * 100)
elif op==5:
    print("50 rs vada pav")
    qty = int(input("Enter qty =>"))
    print("Bill of vada pav = ", qty * 50)
else:
    print("wrong opt")