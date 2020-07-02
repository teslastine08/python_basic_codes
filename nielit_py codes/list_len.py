x=list("ankan")
i=x[0]
j=x[1]
for i in list(x):
    print(i)
    for j in list(x):
        if(x[i]==x[j]):
            x.remove(x[j])
print(i)

