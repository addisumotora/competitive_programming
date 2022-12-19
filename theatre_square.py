import math 

def theatre_square(n,m,a):
    n=math.ceil(n/a)
    m=math.ceil(m/a)
    return n*m

print(theatre_square(6,6,4))