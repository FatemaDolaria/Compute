from itertools import permutations

L = input("Enter first string: ")
M = input("Enter second string: ")
N = input("Enter third string: ")
x = L + M
count = 0

a=permutations(x) 

for i in list(a):
    # join all the letters of the list to make a string 
    #print("".join(i)) 
        if  N == ("".join(i)) :
            count = 1
            break

if count>0 :
    print("Yes")
else:    
    print("No")