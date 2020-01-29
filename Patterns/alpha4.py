n = int(input())
i = 1
while i <= n:
    j = 1
    charT = (n - i + 1)
    while j <= i:
        charTar = chr(charT + 65 - 1)
        print( charTar , end = '')
        j += 1
        charT += 1
    print()
    i += 1



 #OUTPUT
# 5
#E
#DE
#CDE
#BCDE
#ABCDE   
