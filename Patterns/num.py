n = int(input())
print(1)
i = 2
while i <= n:
    j = 1
    while j <= i:
        if ( j == i or j == 1):
            print(i-1 , end = '')
        else :
            print(0 , end = '')
        j += 1
    print()
    i += 1

#OUTPUT
# 5
#
#1
#11
#202
#3003
#40004   
