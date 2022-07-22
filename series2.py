def series2(n):
    num1 = 1
    num2 = 5
    if n <= 0:
        print("Invalid number")
    else:
        for i in range(1, n+1):
            if i%2 != 0:
                print(num1, end = " ")
                num1 -= 5

            else:
                print(num2, end = " ")
                num2 += 3

n = int(input("Enter n: "))
print(series2(n), end = " ")