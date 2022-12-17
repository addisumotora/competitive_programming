def insertionSort1(n, arr):
    for i in range(1,n):
        num = arr[i]
        j=i
        while arr[j-1]> num and j>0:
            arr[j] = arr[j-1]
            j-=1
        arr[j] = num
    return arr

    # for i in range(1,n):
    #     num = arr[i]
    #     for j in range(i,-1,-1):
    #         if arr[j-1]>num:
    #             arr[j] = arr[j-1]
    #         else:
    #             arr[j]=num
    #             break
    #         print(arr) 
    # return arr

print(insertionSort1(5,[2,4,6,8,3]))