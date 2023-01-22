def revolt():
    
    n = eval(input())
    
    for i in range(n):
        lngth = eval(input())
        
        arr = list(map(int, input().split()))
        temp = 0
        n = len(arr)
        l,r = 0, n-1

        

        while r < n:
            if int(arr[l]) > int(arr[r]):
                arr[l],arr[r] = arr[r],arr[l]
                temp += 1
                l += 1
                r += 1
            elif

        print(temp)
             

revolt()