k = int(input())
i = 1
while i <= k:
    st_char = chr(ord('A') + i - 1)
    j = 1
    while j <= k:
        charP = chr(ord(st_char) + j - 1)
        print(charP , end = '')
        j += 1
    print()
    i += 1
    
#OUTPUT
#5
#ABCDE
#BCDEF
#CDEFG
#DEFGH
#EFGHI    
