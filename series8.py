def series8(n):
    l = [0,1]
    for i in range(2,n+1):
        if i%2 != 0:
            fact = 1
            for j in range(1, i):
                fact *= j
            l.append(fact)
        else:
            l.append(l[i-1] + l[i-2])
    print(*l[1:])

n = int(input("Enter n: "))
series8(n)

'''
Enter n: 6
1 1 2 3 24 27
'''