no=int(input("Enter limit =>"))
s=0
for i in range(no,0,-1):
    print(i,end="*")
    s=s*i
print("\nTotal=",s)