class sum_son:
    def __init__(self):
        n = 6
        a = [0, -2, 11, -4, 13, -5, -2]
        dp = [0] * 7

        def maxSubSum():
            dp[0] = 0
            for j in range(1, n + 1):
                dp[j] = max(dp[j - 1] + a[j], a[j])

        def dispmaxSum():
            maxj = 1
            for j in range(2, n + 1):
                if dp[j] > dp[maxj]:
                    maxj = j
            for k in range(maxj, 0, -1):
                if dp[k] <= 0:
                    break
            print("最大连续子序列和: {}".format(dp[maxj]))
            print("所选子序列:",end="")
            for i in range(k+1,maxj+1):
                print(a[i],end=" ")

        maxSubSum()
        dispmaxSum()

if __name__ == '__main__':
    s=sum_son()