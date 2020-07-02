x,y=map(int,input().split())
a=0
b=0
for i in range(x,y):
    if(i%2==0):
        print(i,end="")
        a=i+a
    else:
        print(i,end=")
        b=b+i
print(" sum even: ",a)
print(" sum odd: ",b)

