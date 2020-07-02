print("enter 3 nos.")
a,b,c=map(int,input().split())
if(a>b and a>c and b!=c):
    print("a is greatest")
elif(b>a and b>c and a!=c):
    print("c is greatest")
elif(c>b and c>a and b!=a):
    print("c is greatest")
else:
    if(a==b and a!=c):
        print("a nd b are equal")
    elif(b==c and b!=a):
        print("b and c are equal")
    elif(c==a and c!=b):
        print("c and a are equal")
    else:
        print("all nos are equal")
