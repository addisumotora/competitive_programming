
from math import radians


def insertionSort1(n, arr):
    curr = arr[n-1]
    i = n-2
    while(i>2):
        if arr[i]>=curr:
            arr[i+1]=arr[i]
        else:
            arr[i+1]=curr
            i=-1
        for j in range(n):
            print(arr[j],end=" ")
        print()

        if i==0:
            arr[i]=curr
            for k in range(n):
                print(arr[k],end=" ")
            print()
        i=i-1

insertionSort1(10,[2,3,4,5,6,7,8,9,10,1])