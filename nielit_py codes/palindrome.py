x=int(input("enter a 3 digit no:"))
a=x//100
b=((x%100)//10)
c=((x%100)%10)
d=((c*100)+(b*10)+a)
if(x==d):
    print("palindrome no.")
else:
    print("no is not palindrome")
