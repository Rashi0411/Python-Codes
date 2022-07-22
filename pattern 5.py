n = int(input("Enter n:"))
for i in range(n-1,0,-1):
    for j in range(i,0,-1):
        print(j,end = " ")
    print()

#Enter n: 5
#4 3 2 1
#3 2 1
#2 1
#1
