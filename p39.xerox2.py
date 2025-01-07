print("press 1 for print")
print("press 2 for typing")
op=int(input("Enter opt =>"))
if op==1:
    print("5 rs print")
    qty = int(input("Enter qty =>"))
    if qty>50:
        print("5 rs print")
        print("Bill of print = ", qty * 5)
    elif qty<50:
        print("8 rs print")
        print("Bill of print = ", qty * 8)
    else:
        print("wrong opt")
elif op==2:
    print("15 rs typing")
    qty = int(input("Enter qty =>"))
    if qty>50:
        print("15 rs typing")
        print("Bill of typing = ", qty * 15)
    elif qty<50:
        print("20 rs typing")
        print("Bill of typing = ", qty * 20)
    else:
        print("wrong opt")
else:
    print("wrong opt")