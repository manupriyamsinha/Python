n = int(input())
n1 = (n + 1)// 2
n2 = n1 - 1
#for first half pattern
i = 1
while i <= n1:
    #for spaces
    spaces = 1
    while spaces <= (n1 - i):
        print(' ' , end = '')
        spaces += 1
    #for stars
    j = 1
    while j <= (2 * i) - 1:
        print('*' , end = '')
        j += 1
    print()
    i += 1
#for second half
q = n2
while q >= 1:
    #for spaces
    spaces = 1
    while spaces <= (n2 - q + 1):
        print(" " , end = '')
        spaces += 1
    #for stars
    j = 1
    while j <=  (2 * q ) - 1:
        print('*', end = '')
        j += 1
    print()
    q -= 1


#OUTPUT
    7
   *
  ***
 *****
*******
 *****
  ***
   *
            
