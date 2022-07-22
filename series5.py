n = int(input("Enter n: "))
num = 0
for i in range(1,n+1):
    num = i**i - num
    print(num, end = " ")