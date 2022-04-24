class active:
    def __init__(self):
        flag = [False] * 20
        n = 11
        A = [[0, 0], [1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 15]]

        def solve():
            A.sort(key=lambda x: x[-1])
            preend = 0
            for i in range(1, n + 1):
                if A[i][0] >= preend:
                    flag[i] = True
                    preend = A[i][1]

        solve()
        print("产生最大兼容活动集合")
        for j in range(1, n + 1):
            if flag[j] is True:
                print("活动{}".format(j))


if __name__ == '__main__':
    s = active()
