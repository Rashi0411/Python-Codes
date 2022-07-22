def series1(n):
    first_term = 1
    mul = 1
    for i in range(1,n+1):
        first_term *= mul
        mul += 1
    return first_term

n = int(input("Enter n: "))
print(1, end = " ")
for i in range(1,n+1):
    print(series1(i), end = " ")