def factorial(c):
    if c==0:
        r=1
    else:
        c=c*factorial(c-1)
     return r
n=int (input("enter the no: "))
print("factorial of {} is {}: ".format(n,factorial(n)))
