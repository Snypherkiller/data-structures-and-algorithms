def bubbleSort(arr):
    n=len(arr)

    for k in range (0,n):
        for i in range (0,n-k-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]

arr=[20,10,40,30,50,80,60,70,90,100,110,150,140]

print("Before sorting : {}".format(arr))
bubbleSort(arr)
print("After sorting : {}".format(arr))