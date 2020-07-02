from array import *
a=array('i',[1,2,3,4,5,6,7,8,9])
for i in a:
    print(i,end=" ")
a.remove(4)
print(a)

print("the popped one is: ",a.pop(2))
print(a)

print("indexing at 5 : ",a[6])

a.append(4)
print("new array: ",a)

a.extend([42,65,98])
print("extended array: ",a)
