#char_pattern
k = int(input())
i = 1

while i <= k:
    j = 1
    while j <= k:
        charT = chr(ord('A') + j - 1)
        print(charT , end = '')
        j += 1
    print()
    i += 1
    
#OUTPUT                    
#5
#ABCDE
#ABCDE
#ABCDE
#ABCDE
#ABCDE
