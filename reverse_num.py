
def reverse(n):
    rev = 0
    while n > 0:
        a = n % 10
        rev = (rev * 10) + a
        n = n // 10
    return rev
pass	

n=int(input())
result = reverse(n)
print(result)

#-----------2nd method-------
#revers 2
def reverse(n):
    rev = 0
    while n > 0:
        a = n % 10
        rev = (rev * 10) + a
        n = n // 10
    return rev
    

n=int(input())
result = reverse(n)
print(result)
