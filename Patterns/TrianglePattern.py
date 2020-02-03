n = int(input())
i =1
while i <=  n:
    #spacing
    spaces = 1
    while spaces <= ( n - i):
        print(' ' ,end ='')
        spaces += 1
    j = 1
    p = i
    while j <= i:
        print(p , end = '')
        j += 1
        p += 1
    p = ((2 * i ) - 2)
    while p >= i :
        print(p , end = '')
        p -= 1
    print()
    i += 1


#OUTPUT
 #   6

#    1
 #   232
#  34543
 # 4567654
# 567898765
#67891011109876
