# Read input as sepcified in the question
# Print output as specified in the question

## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
##      print(val1, " ", val2)

#start F value
S = int(input())
#end F value
E = int(input())
#step size
W = int(input())

while S <= E:
    c = (S - 32) * 5 / 9 
    #print(S , "\t" , int(c))
    print(str(S) +"\t" + str(int(c)))
    S += W 
