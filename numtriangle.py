val=int(input('Enter row of right triangle:'))
for i in range(val):
    for j in range(i+1):
        print(j+1,end=" ")
    print()