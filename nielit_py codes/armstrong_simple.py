n=input("enter the no")
if (sum([int(i)**len(n) for i in n])==int(n)):
    print (n,'is armstrong')
else:
    print (n,'isn"'"t"'"armstrong')
