def bubblesort(arr):
    for i in range((len(arr)-1),1,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

arr=[9,10,2,3,4]
sorted_num=bubblesort(arr)
print(arr)


