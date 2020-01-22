n = int(input())

even_sum = 0
odd_sum = 0
while n > 0:
    a = n % 10
    n = n // 10
    if a % 2 == 0:
        even_sum += a
    else:
        odd_sum += a
print(even_sum , ' ' , odd_sum)       
        
