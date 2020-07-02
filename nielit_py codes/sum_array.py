from array import *
t=0
a=array('i',[])
n=int(input("enter array size: "))
for i in range (n):
    a.append(int(input()))

for i in range(n-1):
    for j in range(n-1-i):
        if a[j]>a[j+1]:
            t=a[j];
            a[j]=a[j+1]
            a[j+1]=t
print(a)
