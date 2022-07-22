def series7(a,b,c,n):
    l = [0,3,5,7]
    for i in range(4,n + 1):
        l.append(l[i-3]+l[i-2]-l[i-1])
    print(*l[1:])

n = int(input("Enter n: "))
series7(3,5,7,n)

'''
Enter n: 9
3 5 7 1 11 -3 15 -7 19
'''