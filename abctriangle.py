val=int(input('Enter row of right triangle:'))
ascii=65
for i in range(val):
    for j in range(i+1):    
        let=chr(ascii)
        print(let,end=" ")
    ascii+=1
    print()