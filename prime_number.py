n=int(input('Enter number to check prime number are not:'))
if n==1:
    print('1 is neither prime nor composite number')
else:
    count=0
    for i in range(1,n):
        if n%i==0:
            count+=1
    if count<2:
        print('given number is prime number')
    else:
        print('it is not a prime numbber')