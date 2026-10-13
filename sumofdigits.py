n=int(input('Enter digits:'))
sum=0
while n>0:
    digits=n%10
    sum+=digits
    n=n//10
print(sum)

