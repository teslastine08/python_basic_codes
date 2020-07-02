a=1
def myfunc():
    global a
    print("global a: ",a)
    a=2
    print("global a modified: ",a)
myfunc()
a=1
print("new global a: ",a)
