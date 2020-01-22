 ## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
a = 0
b = 1
x = 2

#Fibonacci
if n < 0:
    print("Incorrect input")
elif n == 0:
    print(a)
elif n == 1:
     print(b)
else:
    while x <= n:
        c = a + b
        a = b
        b = c
        x += 1
    print(c)        
        
