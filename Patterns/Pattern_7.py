n = int(input())
i = 1
p = i
while i <= n:
    j = 1
    while j <= i:
        print(p , end = '')
        j += 1
        p += 1
    print()
    i += 1


#Output
# 4
#1
#23
#456
#78910
