x={}
n=int(input("enter the no of keys:"))
for i in range (n):
    print("enter the key:", end='')
    k=input()
    print("enter the values:",end='')
    v=input()
    x.update({k:v})
print(x)
