from array import *
a=array('i',[])
n=int(input("enter the array size: "))
for i in range (n):
    a.append(int(input()))
for i in range(n):
    for j in range(n-1):
        if(a[i]>a[j]):
            t=a[i]
            a[i]=a[j]+1
            a[j]=t
            
print(a)
