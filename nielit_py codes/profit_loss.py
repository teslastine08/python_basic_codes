print("enter the cost price and sell price simultaneously: ")
a,b=map(int,input().split())
if(b>a):
    print("profit by an amount of: ",(b-a))
else:
    print("loss by an amount of: ",(a-b))
