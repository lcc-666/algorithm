class bag:
    def __init__(self):
        n = 4
        W = 6
        w = [0, 5, 3, 2, 1]
        v = [0, 4, 4, 3, 1]
        x = [0] * 20
        op = [0] * 20
        maxv=[0]

        def dfs(i, tw, tv, op):
            if i > n:
                if tw <= W and tv > maxv[0]:
                    maxv[0] = tv
                    for j in range(1, n + 1):
                        x[j] = op[j]

            else:
                if tw + w[i] <= W:
                    op[i] = 1
                    dfs(i + 1, tw + w[i], tv + v[i], op)
                op[i] = 0
                dfs(i + 1, tw, tv, op)

        dfs(1, 0, 0, op)
        for i in range(1,n+1):
            if x[i]==1:
                print("选取第%d个物品"%i)
        print(W, maxv[0])


if __name__ == '__main__':
    s = bag()
