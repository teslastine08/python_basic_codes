x=int(input("enter no. of telephone calls:"))
if(x<=100):
    print("bill is free")
elif(x>100 and x<=200):
    print("first 100 calls: free")
    print("total: ",(x-100)*.80)
elif(x>200 and x<=300):
    print("first 100 calls: free")
    print("total: ", (x-200)*1.80+80)
else:
    print("first 100 calls: free")
    print("total: ", (x-300)*2.30+180+80)
    
