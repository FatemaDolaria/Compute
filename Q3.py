'''Given a permutation ‘a’ of length ‘n’, your task is to find out a lexicographically smallest 
permutation ‘b’ of length ‘n’ such that it is different from ‘a’ at every position 
i.e. a[1] ≠ b[1], a[2] ≠ b[2],.....,a[n]≠ b[n]'''

# Code 1

n = int(input())
if n == 1 :
    print('-1')

else :
    f = []
    for i in range(1,n+1) :
        f.append(i)
    
    f.sort(reverse=True)
    f.pop()

    f.sort()
    f.append(1)

    #for i in range(len(f)) :
    print(f)



# Code 2

n = int(input())
if n == 1 :
    print('-1')

else :
    f = []
    for i in range(1, n+1) :
        f.append(i)

    f.pop(0)
    f.append(1)

    print(f)