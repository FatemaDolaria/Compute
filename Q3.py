'''Given a permutation ‘a’ of length ‘n’, your task is to find out a lexicographically smallest 
permutation ‘b’ of length ‘n’ such that it is different from ‘a’ at every position 
i.e. a[1] ≠ b[1], a[2] ≠ b[2],.....,a[n]≠ b[n]'''

n = int(input())
if n == 1 :
    print('-1')