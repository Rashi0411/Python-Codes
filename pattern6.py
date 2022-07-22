n = int(input("Enter n:"))
for i in range(n-1,0,-1):
    for j in range(i):
        print(i,end=" ")
    print()

#Enter n:6
#5 5 5 5 5
#4 4 4 4
#3 3 3
#2 2
#1
