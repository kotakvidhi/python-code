print("press 1 for green")
print("press 2 for yellow")
print("press 3 for red")
op=int(input("Enter opt =>"))
if op==1:
    print("car is allowed to go.")
elif op==2:
    print("car has to wait.")
elif op==3:
    print("car has to stop.")
else:
    print("unrecognized signal")