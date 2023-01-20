
def petrya():
    interlen = eval(input())
    output = [0] * interlen
    arr = input()
    arr = arr.split(' ')

    for i in range(interlen):
        p = arr[i]
        output[int(p)-1] = i + 1

    for i in output:
        print(i, end=' ')
    print()

petrya()