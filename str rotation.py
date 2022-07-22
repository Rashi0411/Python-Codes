def stringRot(str, N):
    ans = ''
    n = 0
    for i in range(N):
        n = sum(pow(N,2))
        if n%2==0:
            ans += str[-1::-2]+[::-1]
        else:
            ans += str[i+2:1:]+[i:i+2:]
    return ans


str,N= map(int, input().split(':'))
print(stringRot(input(), str, N))