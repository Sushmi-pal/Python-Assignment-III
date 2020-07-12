def linearsearch(arr,n):
    for i in range(len(arr)):
        if arr[i]==n:
            print('{} is found in index {}'.format(n,i))
            break

    else:
        print('{} is not found'.format(n))

linearsearch([10,50,30,70,80,60,20,90,40],100)
