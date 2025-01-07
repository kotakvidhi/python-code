import random
right=0
wrong=0
for i in range(1,6):
    no1=random.randint(1,20)
    no2=random.randint(1,20)
    print("No1=",no1," No2=",no2)
    add=int(input("Enter add =>"))
    if add == no1+no2:
        print("right")
        right+=1
    else:
        print("wrong")
        wrong+=1
        print("Total right answer=",right)
        print("Total wrong answer=",wrong)
