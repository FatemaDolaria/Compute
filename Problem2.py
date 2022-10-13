N = int(input("Enter number of buckets: "))
O = []
T = []
sum = 0
i = 0
while i < N:
    #print(i)
    a = int(input("Remaining volume in bucket " + str(i+1) + ":"))
    b = int(input("Total volume of bucket" + str(i+1) + ": "))
    if (a > b):
        print("Invalid input. Please re-enter the values")
        continue
    else:
        T.append(b)
        O.append(b-a)
        sum = sum + (b-a)
        i += 1

'''print(O)
print(T)
print(sum)'''

T.sort(reverse=True)
#print(T)

if (sum <= (T[0] + T[1])):
    print("Yes")
else:
    print("No")
