print(1, end=" ")
for Number in range (1, 101):
    c = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            c = c + 1
            break

    if (c == 0 and Number != 1):
        print(" %d" %Number, end = '  ')
