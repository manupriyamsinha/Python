n = int(input())
i = 1
while i <= n:
    spaces = 1
    #spacing
    while spaces <= ( n  - i):
        print(' ' , end = '')
        spaces += 1
    #increasing sequence
    j = 1
    p = 1
    while j <= i:
        print(p , end = '')
        j += 1
        p += 1
    #decreasing sequence
    p = i - 1
    while p >= 1:
        print(p , end = '')
        p -= 1
    print()
    i += 1


#OUTPUT
    
#7
    #  1
  #   121
 #   12321
 #  1234321
#  123454321
# 12345654321
#1234567654321
