n = int(input("Enter n: "))
for i in range(1, n+1):
    ans = 0
    for j in range(1, i+1):
        ans += (i**j)
    print(ans, end = " ")