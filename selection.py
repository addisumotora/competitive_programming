def selectionSort(arr,n):

    for i in range(n):
        num = i
        for j in range(i+1,n):
            if arr[num]>arr[j]:
                num = j
        arr[i],arr[num] = arr[num],arr[i]
    return arr

print(selectionSort([4,1,3,9,7],5))