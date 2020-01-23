n = int(input())
i = 1
while i <= n:
    #print ith row
    j = 1
    while j <= n:
        #print jth column
        print("*", end = '')#print by-default changes line after every use. So, we changed it using end ='' , a blank so that it doesn't change line.
        j += 1   
    print()#to change line after every column is complete    
    i += 1
