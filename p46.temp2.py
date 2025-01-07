temp=float(input("Enter temperature =>"))
if temp < 0:
    print("freezing atmosphere")
elif 0 < temp <= 10:
    print("very cold atmosphere")
elif 10 < temp  <= 20:
    print("cold atmosphere")
elif 20 < temp <= 30:
    print("normal atmosphere")
elif 30 < temp <= 40:
    print("hot atmosphere")
else:
    print("very hot atmosphere")