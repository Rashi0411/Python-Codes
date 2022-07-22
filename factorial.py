n = int(input("Enter n: "))
num = 1
for i in range(1,n+1):
    num *= i
print("The factorial of",n,"is",num)