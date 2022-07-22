def prime(n):
    count = 0
    for i in range(1,n+1):
        if n%i == 0:
            count += 1
    if count == 2:
        return i

def series9(n):
    l = []
    c= 0
    for i in range(2,n+1):
        if prime(i):
            l.append(i)
            c=c+1
        elif c % 2 == 0:
            l.append(l[-1] * l[-2])

    print(*l)

n = int(input("Enter n: "))
series9(n)
