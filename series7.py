#Using recursion
def series7(a,b,c,n):
    if n == 1:
        return a
    elif n == 2:
        return b
    elif n == 3:
        return c
    else:
        return series7(a,b,c,n-3) + series7(a,b,c,n-2) - series7(a,b,c,n-1)

n = int(input("Enter the value of n: "))
for i in range(1,n+1):
    print(series7(3,5,7,i),end = " ")

'''
Enter the value of n: 8
3 5 7 1 11 -3 15 -7 
'''