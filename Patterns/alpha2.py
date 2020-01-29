k = int(input())
i = 1
x = ord('A')
while i <= k:
    j = 1
    while j <= k:
        chara = (x + j - 1)
        chTarget = chr(chara)
        print(chTarget , end = '')
        j += 1
    print()
    x += 1
    i += 1



#OUTPUT
#5
#ABCDE
#BCDEF
#CDEFG
#DEFGH
#EFGHI
