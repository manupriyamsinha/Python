n = int(input())
while n != 6:
   
    if n == 1:
        x = int(input())
        y = int(input())
        sum = x + y
        print(sum)

    elif n == 2:
        x = int(input())
        y = int(input())
        sub = x - y
        print(sub)

    elif n == 3:
        x = int(input())
        y = int(input())
        prod = x * y
        print(prod)

    elif n == 4:
        x = int(input())
        y = int(input())
        quo = x // y
        print(quo)

    elif n == 5:
        x = int(input())
        y = int(input())
        rem = x % y
        print(rem)

    else:
        print("Invalid Operation")
    n = int(input())     
