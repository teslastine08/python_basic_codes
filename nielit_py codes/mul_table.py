from array import *
a=array("i",[])
n=int(input("enter the array size"))
for i in range (n):
    a.append(int(input("enter the element: ")))
    for elements in a:
        print(elements,end="")
