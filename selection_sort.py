
def selectionSort(arr,n):
    for i in range(n):
        for j in range(i):
            if arr[i]<arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr


print(selectionSort([9,7,4,3,1],5))