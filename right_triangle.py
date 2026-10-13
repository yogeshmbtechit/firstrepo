val=int(input('Enter row of right triangle:'))
for i in range(0,val+1):
    for j in range(0,i):
        print("*",end=" ")
    print()