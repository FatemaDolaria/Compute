'''Given two positive integers ‘a’ and ‘b’, find the minimum number of moves required to make ‘a’ divisible by ‘b’. 
In one move you can increment a by 1 (replace a by a+1))'''

# Code 1

print("Enter dividend and divisor: ")
a = int(input())
b = int(input())
i = 0
while (a%b != 0) :
    a += 1
    i += 1
print(i)



# Code 2

print("Enter dividend and divisor: ")
a = int(input())
b = int(input())

for i in range(0, b) :
    if a%b == 0 :
        print(i)
        break
    else :
        a += 1