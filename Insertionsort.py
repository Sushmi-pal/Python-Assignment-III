def insertionsort(arr):
    for i in range(len(arr)):
        for j in range(i,0,-1):
            if arr[j] == arr[0]:
                arr[j]

            if arr[j]<arr[j-1]:
                temp=arr[j-1]
                arr[j-1]=arr[j]
                arr[j]=temp

arr=[12,11,13,5,6]
insertionsort(arr)
print(arr)