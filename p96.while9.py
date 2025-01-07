while True:
    print("Press 1 for add")
    print("Press 2 for sub")
    print("Press 1 for mul")
    print("Press 2 for div")
    op = int(input("Enter op =>"))
    if op==1:
        no1 = int(input("Enter no1 =>"))
        no2 = int(input("Enter no2 =>"))
        print("add=",no1+no2)
    elif op==2:
        no1 = int(input("Enter no1 =>"))
        no2 = int(input("Enter no2 =>"))
        print("sub=",no1-no2)
    elif op==3:
        no1 = int(input("Enter no1 =>"))
        no2 = int(input("Enter no2 =>"))
        print("mul=",no1*no2)
    elif op==4:
        no1 = int(input("Enter no1 =>"))
        no2 = int(input("Enter no2 =>"))
        print("sub=",no1/no2)
    elif op==5:
        print("bye")
        break
    else:
        print("wrong opt")