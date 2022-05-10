def selectionSort(arr,n):
    for i in range(n):
        for j in range(n):
            if arr[i]<arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    for i in range(n):
        print(arr[i],end=" ")

                

selectionSort([4, 1, 3,9, 7],5)