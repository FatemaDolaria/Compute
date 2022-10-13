import math

def PerfectSquare(x):
    sqrt = math.sqrt(x)
    return int(sqrt)**2 == x

n = int(input("Enter a number: "))
if PerfectSquare(n):
    print("Yes")
else:
    print("No")
