x=int(input("enter a 3 digit no."))
a=x//100
b=((x%100)//10)
c=((x%100)%10)
d=((c**3)+(b**3)+(a**3))
if(d==x):
    print("no is armstrong")
else:
    print("no. is not armstrong")
