#Print N pattern
#take input from user 
n = int(input())
i = 1
#loop for row
while i <= n:
    j = 1
    #loop for column
    while j <= n:
        print(n, end = '')
        j += 1
    print()    
    i +=1     
