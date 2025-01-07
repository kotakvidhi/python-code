pizza_qty=0
burger_qty=0
coke_qty=0
while True:
    print("press 1 for pizza")
    print("press 2 for burger")
    print("press 3 for coke")
    print("press 4 for exit")
    op = int(input("Enter op =>"))
    if op==1:
        print("180 rs pizza")
        qty=int(input("Enter qty =>"))
        print("Bill of pizza=",qty * 180)
        pizza_qty += qty
    elif op==2:
        print("120 rs burger")
        qty=int(input("Enter qty =>"))
        print("Bill of burger=",qty * 120)
        burger_qty += qty
    elif op==3:
        print("100 rs coke")
        qty=int(input("Enter qty =>"))
        print("Bill of coke=",qty * 100)
        coke_qty += qty
    elif op==4:
        Total_qty =(pizza_qty*180)+(burger_qty*120)+(coke_qty*100)
        print("Total amount",Total_qty)
        break
    else:
        print("wrong op")

