n=int(input('Enter digits:'))
original=n
rev=0
while n>0:
    rev=rev*10+n%10 
    n=n//10
print(rev)
if rev==original:
    print('it is a palindrome')
else:
    print('it is not a palindrome')