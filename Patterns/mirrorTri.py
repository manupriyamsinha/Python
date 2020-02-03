#mirror
n = int(input())
i = 1
while i <= n:
    j = 1
    k = 1
    #spacing
    while k <= n - i:
            print(' ' , end = '')
            k += 1
    #stars printing
    while j <= i:
        print('*', end = '')
        j += 1
    print()
    i += 1
    

#OUTPUT
    7
      *
     **
    ***
   ****
  *****
 ******
*******
