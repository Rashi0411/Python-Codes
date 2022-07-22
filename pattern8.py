n = int(input("Enter n:"))
for i in range(1,n+1):
    for j in range(0,i):
        print(1+j,end=" ")
    print()
#Enter n: 5
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5