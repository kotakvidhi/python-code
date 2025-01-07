no=int(input("Enter limit =>"))
s=0
for i in range(1,no+1):
    print(i,end="*")
    s=s*i
print("\nTotal=",s)