def add(a,b):
    c=a+b 
    print("addition of two numbers are:",c)
def sub(a,b):
    c=a-b
    print("Subtraction of two  number is:",c)
def  mul(a,b):
    c=a*b 
    print("multiplication of  two number is:",c)
def div(a,b):
    c=a/b
    print('division of wo number is:')
a=int(input("enter  first number:"))
b=int(input("Enter second nnumber:"))
c=input("enter operation (+,-,*,/):")
if  c=="+": add(a,b)
if  c=="-": sub(a,b)
if  c=="*": mul(a,b)
if  c=="/": div(a,b) 
else : print("operation not mentioned")

