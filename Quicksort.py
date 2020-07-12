def partition(arr,start,end):
    pivot=arr[start]
    low=start+1
    high=end

    while True:
        while low <= high and arr[start] < pivot:
            low = low+1

        while low <= high and arr[high] > pivot:
            high = high-1

        if low <= high:
            arr[low],arr[high] = arr[high],arr[low]

        else:
            break

    pivot,arr[high] =arr[high],pivot
    return high

def quick_sort(arr, start, end):
    if start<end:
        p = partition(arr, start, end)
        quick_sort(arr, start, p-1)
        quick_sort(arr, p+1, end)

arr = [35,50,15,25,80]
quick_sort(arr, 0, len(arr) - 1)
print(arr)

