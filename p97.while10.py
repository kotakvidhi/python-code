while True:
    print("press 1 for pizza")
    print("press 2 for burger")
    print("press 3 for coffee")
    print("press 4 for cake")
    op = int(input("Enter op =>"))
    if op==1:
        print("180 rs pizza")
        qty=int(input("Enter qty =>"))
        print("Bill of pizza=",qty * 180)
    elif op==2:
        print("120 rs burger")
        qty = int(input("Enter qty =>"))
        print("Bill of burger=",qty * 120)
    elif op==3:
        print("90 rs coffee")
        qty = int(input("Enter qty =>"))
        print("Bill of coffee=",qty * 90)
    elif op==4:
        print("500 rs cake")
        qty = int(input("Enter qty =>"))
        print("Bill of cake=", qty * 500)
    elif op==5:
        print("Exit")
        break
    else:
        print("wrong opt")
