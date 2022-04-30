class num:
    def __init__(self):
        MAX = 6
        dp = []
        for i in range(MAX):
            dp.append([0] * MAX)

        def dpf(n, k):
            if dp[n][k] != 0:
                return dp[n][k]
            if n == 1 or k == 1:
                dp[n][k] = 1
                return dp[n][k]
            elif n < k:
                dp[n][k] = dpf(n, n)
                return dp[n][k]
            elif n == k:
                dp[n][k] = dpf(n, k - 1) + 1
                return dp[n][k]
            else:
                dp[n][k] = dpf(n, k - 1) + dpf(n - k, k)
                return dp[n][k]

        dpf(5, 5)
        print(dp[5][5])


if __name__ == '__main__':
    s = num()
