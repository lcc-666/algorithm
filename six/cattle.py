class Cow:
    def __init__(self):
        n = 5
        A = [[0, 0, 0], [1, 1, 10], [2, 2, 4], [3, 3, 6], [4, 5, 8], [5, 4, 7]]
        A.sort(key=lambda x: (x[-1], x[-2]))
        ans = [0] * 6

        def solve():
            num = 1
            for i in range(1, n + 1):
                if ans[i] == 0:
                    ans[i] = num
                    preend = A[i][-1]
                    for j in range(i + 1, n + 1):
                        if A[j][-2] > preend and ans[j] == 0:
                            ans[j] = num
                            preend = A[j][-1]
                    num += 1

        solve()
        print("求解结果")
        for i in range(1, n + 1):
            print("牛{}安排的蓄栏:{}".format(A[i][0], ans[i]))


if __name__ == '__main__':
    c = Cow()
