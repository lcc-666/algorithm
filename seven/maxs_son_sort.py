class sort:
    def __init__(self):
        a = [2, 1, 5, 3, 6, 4, 8, 9, 7]
        n = len(a)
        dp = [0] * n

        def solve(a, n):
            for i in range(0, n):
                dp[i] = 1
                for j in range(0, i):
                    if a[i] > a[j]:
                        dp[i] = max(dp[i], dp[j] + 1)
            ans = dp[0]
            for i in range(1, n):
                ans = max(ans, dp[i])
            return ans
        ans=solve(a,n)
        print("最长递增子序列和为{}".format(ans))

if __name__ == '__main__':
    s=sort()
