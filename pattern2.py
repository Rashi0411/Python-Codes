n = int(input())
for i in range(0,n+1):
    for j in range(0,i+1):
        print(j+i,end = " ")
    j += 1
    print()

#5
#0
#1 2
#2 3 4
#3 4 5 6
#4 5 6 7 8
#5 6 7 8 9 10
