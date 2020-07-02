def eliza(c):
    print("Hi {}".format(c))
eliza("Ankan")
pas={"Ankan":12345}
i=int(input("enter pass: "))
if (i==12345):
    print("Access")
    print("enter the no :")
    x=int(input())
    x=x**3
    print(x)
else:
    print("Access denied")
