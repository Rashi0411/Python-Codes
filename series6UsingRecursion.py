def prime(n):
    c = 0
    for i in range(1,n+1):
        if n%i == 0:
            c += 1
    if c == 2:
        return True
    else:
        return False

def series6(a,b,c,n):
    if n == 1:
        return a
    elif n == 2:
        return b
    elif n == 3:
        return c
    elif (prime(n)):
        return n - series6(a,b,c,n-1)
    else:
        return series6(a,b,c,n-1) + series6(a,b,c,n-2) - series6(a,b,c,n-3)

n = int(input("Enter n: "))
if n < 3:
    print("INVALID!")
else:
    for i in range(1,n + 1):
        print(series6(1,2,3,i), end = " ")