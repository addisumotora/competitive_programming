def insertionSort1(n, arr):
    for i in range(1,n):
        num = arr[i]
        j=i
        while arr[j-1]> num and j>0:
            arr[j] = arr[j-1]
            j-=1
        arr[j] = num
    return arr