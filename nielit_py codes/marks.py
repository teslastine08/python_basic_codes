from array import *
a=array('i',[50,60,70,80,90])
for i in a:
    print(i)
n=len(a)
s=sum(a,n)
print("total: ",s)
print("average: ",s/(n))
