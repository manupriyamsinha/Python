n = int(input())
i = 1
x = ord('A')
while i <= n:
    j = 1
    while j <= i:
        charT = x + j - 1
        charTar = chr(charT)
        print(charTar , end = '')
        j += 1
    print()
    i += 1
    x += 1


#OUTPUT
#4
#A
#BC
#CDE
#DEFG    
