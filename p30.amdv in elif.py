print("press 1 for add")
print("press 2 for sub")
print("press 3 for mul")
print("press 4 for div")
op=int(input("Enter opt =>"))
if op==1:
   no1=int(input("Enter no1 =>"))
   no2=int(input("Enter no2 =>"))
   print("Add=",no1+no2)
elif op==2:
    no1=int(input("Enter no1 =>"))
    no2=int(input("Enter no2 =>"))
    print("sub=",no1-no2)
elif op==3:
    no1=int(input("Enter no1 =>"))
    no2=int(input("Enter no2 =>"))
    print("mul=",no1*no2)
elif op==4:
    no1=int(input("Enter no1 =>"))
    no2=(int(input("Enter no2 =>")))
    print("div=",no1/no2)
else:
    print("Wrong opt")