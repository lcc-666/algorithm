class bag:
    def __init__(self):
        n = 5
        W = 10
        MAX = 11
        w = [0, 2, 2, 6, 5, 4] + [0] * MAX
        v = [0, 6, 3, 5, 4, 6] + [0] * MAX
        dp = []
        for i in range(MAX):
            dp.append([0] * MAX)
        x = [0] * MAX
        maxv = [0]

        def Knap():
            for i in range(0, n + 1):
                dp[i][0] = 0
            for r in range(0, W + 1):
                dp[0][r] = 0
            for i in range(1, n + 1):
                for r in range(1, W + 1):
                    if r < w[i]:
                        dp[i][r] = dp[i - 1][r]
                    else:
                        dp[i][r] = max(dp[i - 1][r], dp[i - 1][r - w[i]] + v[i])

        def Buildx():
            i = n
            r = W
            while i >= 0:
                if dp[i][r] != dp[i - 1][r]:
                    x[i] = 1
                    maxv[0] += v[i]
                    r -= w[i]
                else:
                    x[i] = 0
                i -= 1

        Knap()
        Buildx()
        weight = 0
        for i in range(1, 6):
            weight += w[i] * x[i]
        print(x[1:6])
        print("装入物品总重量为{}".format(weight))
        print("总价值为{}".format(maxv[0]))


if __name__ == '__main__':
    s = bag()
