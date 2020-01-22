def checkPalindrome(num):
    r = reverse(num) 
    if num == r:
        return True
    return False
        
	
pass    
def reverse(num):
    rev = 0
    while num > 0:
        a = num % 10
        rev = (rev * 10) + a
        num = num // 10
    return rev
   

num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
