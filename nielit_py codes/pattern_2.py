print("enter the range")
a,e=map(int,input().split(','))
c=0
for i in range(a,e):
    j=i
    a=0
    while(j!=0):
        a=a+(j%10)**3
        j=j//10
    if(i==a):
        print(a)
        c=c+1
    if(c==2):
        break
