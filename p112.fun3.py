def add():
    num1=int(input("Enter a value :"))
    num2=int(input("Enter b value :"))
    print("Add =",num1+num2)

def max2():
    length=float(input("Enter the length of the rectangle =>"))
    breadth=float(input("Enter the breadth of the rectangle =>"))
    if length==breadth:
        print("it is square.")
    else:
        print("it is not a square.")
add()
max2()