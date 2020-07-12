def interpolationsearch(arr,s):
    l=len(arr)
    a=[]
    for i in range(l):
        a.append(i)
    low=a[0]
    high=a[-1]
    if s in arr:
        POS=int(low+((s-arr[low])/(arr[high]-arr[low]))*(high-low))
        print('{} is found in index {}'.format(s,POS))
    else:
        print('{} is not in the list'.format(s))

interpolationsearch([1,3,5,7,9],11)
