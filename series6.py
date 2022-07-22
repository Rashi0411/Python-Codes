def prime(n):
    count = 0
    for i in range(1,n+1):
        if n%i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False

def series6(a,b,c,n):
    l = [0,a,b,c]
    for i in range(4,n+1):
        if(prime(i)):
            l.append(i-l[i-1])
        else:
            l.append(l[i-1]+l[i-2]-l[i-3])
    print(*l[1:])

n = int(input("Enter the value of n: "))
series6(1,2,3,n)

'''
Enter the value of n: 10
1 2 3 4 1 2 5 6 9 10
'''