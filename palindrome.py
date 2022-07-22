n = input("Enter n:")
rev_n = reversed(n)
if list(n) == list(rev_n):
    print(n,"is Palindrome")
else:
    print(n,"is not Palindrome")