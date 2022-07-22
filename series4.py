n = int(input("Enter n: "))
num = 3
print(num, end = " ")
for i in range(0,n-1):
    num += pow(2,i)
    print(num, end = " ")
    