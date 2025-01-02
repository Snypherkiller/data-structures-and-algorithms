def bubbleSort(arr):
    n=len(arr)
    for k in range (0,n):
        for i in range (0,n-k-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
            
arr=[3,5,6,4,2,1]

print("Before sorting : {} ".format(arr))

bubbleSort(arr)

print("After sorting : {} " .format(arr))