age=int(input("Enter your age =>"))
if 0<= age <= 12:
    print("you are a child.")
elif 13 <= age <= 19:
    print("you are a teenager.")
elif 20 <= age <= 64:
    print("you are a adult.")
elif age >= 65:
    print("you are a senior.")