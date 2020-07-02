from array import *
a=array('i',[])
n=int(input("enter array size: "))
for i in range (n):
    a.append(int(input()))

for i in range(n):
    for j in range(n):
        if(a[j]==i+1):
            a.remove(a[i])
            a[j]=a[i-1]
        n=n-1
print(a)
