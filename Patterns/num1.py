n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= i:
        if(j == i or j == 1):
            print(1, end = '')
        else:
            print(2, end = '')
        j += 1
    print()
    i += 1


#OUTPUT
#5

#1
#11
#121
#1221
#12221
