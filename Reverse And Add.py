def reverse(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
        return rev

def isPalindrome(num):
    return (reverse(num) == num)

def ReverseAndAdd(num):
    if (isPalindrome(num)):
        print(num)
    else:
        rev=0
        while(num <= N):
            rev = reverse(num)
            num += rev
            if(isPalindrome(num)):
                print(num)
                break
            else:
                if(num > N):
                    print("Palindrome does not exit for this number!")



N = int(input("Enter the value of N: "))
print(ReverseAndAdd(11))










