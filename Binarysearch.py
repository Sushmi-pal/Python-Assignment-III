def binary_search(arr,s):
    low=0
    high=len(arr)-1

    while high>=low:
        mid=(high+low)//2


        if s==arr[mid]:
            return mid
        elif s>arr[mid]:
            low=mid+1
        else:
            high=mid-1

    else:
        return -1

arr=[]
num=int(input('Enter the number of terms'))
for i in range(num):
    input_num=int(input('Enter num:'))
    arr.append(input_num)
s=int(input('Enter the number to be searched:'))
result=binary_search(arr,s)
print('Searched item is found at {}'.format(result)) if result !=-1 else print('No any item present')

