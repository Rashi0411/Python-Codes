n = int(input("Enter n: "))
length = len(str(n))
sum = 0
temp = n
while(temp > 0):
    digit = temp % 10
    print(digit)
    sum += digit ** length
    print(sum)
    temp //= 10
    print(temp)
if n == sum:
    print("Armstrong")
else:
    print("Not Armstrong")