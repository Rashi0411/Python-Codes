def stringRot(str, N, K):
    ans = ''
    for i in range(0, N, K):
        ans += str[i:i + K:][::-1]
    return ans


N, K = map(int, input().split()
print(stringRot(input(), N, K))
