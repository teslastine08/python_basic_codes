from array import *
def printArray(arr):
  print ((' ').join(str(i) for i in arr))
  
def bubblesort(arr):
  for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
      if arr[j] > arr[j + 1]:
        temp = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = temp
    print ("After pass " + str(i) + "  :",
    printArray(arr))
arr = [10, 7, 3, 1, 9, 7, 4, 3]
print ("Initial Array :",
printArray(arr))
bubblesort(arr)
