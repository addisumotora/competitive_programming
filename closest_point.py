
def closest_point(a,k):
    b = []
    for i in range(len(a)):
       b.append(abs(a[i]))
    print(b)
    print(b[:k])




closest_point([[1,3],[-2,2],[2,-2]],2)