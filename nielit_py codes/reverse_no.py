x=int(input("enter the no."))
Reverse = 0
while(x > 0):
    a=x%10
    Reverse=(Reverse *10)+a
    x=x//10
print("reverse is: ",Reverse)
