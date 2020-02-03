#Isoceles Triangle
n = int(input())
i = 1
while i <= n:
    #spacing
    spaces = 1
    while spaces <= (n - i):
        print(' ', end = '')
        spaces += 1
    #increasing count
    j = 1
    p = 1
    while j <= i:
        print( p , end = '')
        j += 1
        p += 1
    #decreasing count
    p = i - 1
    while p >= 1:
        print(p , end = '')
        p -= 1
    print()
    i += 1
