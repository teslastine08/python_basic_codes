x="ankan"
print(x)
l=len(x)
j=0
for i in range(l):
    k=0
    while k<i:
        print(' ',end='')
        k+=1
    while(j<=i):
        print(x[j],end='')
        j+=1
    print()
