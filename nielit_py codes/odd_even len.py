s="ankan"
l=len(s)
i=-1
for i in range(l):
    if(i%2==0):
        print("odds:")
        print(s[i], end=" ")
for i in range(l):
    if(i%2!=0):
        print("even: ")
        print(s[i], end=" ")
