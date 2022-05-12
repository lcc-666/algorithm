class MGraph:
    def __init__(self):
        INF = float('inf')
        self.n = 4
        self.edges = [[0, 5, INF, 7],
                      [INF, 0, 4, 2],
                      [3, 3, 0, 2],
                      [INF, INF, 1, 0]]


class Floyd:
    def __init__(self):
        INF = float('inf')
        g = MGraph()
        MAXV = 4
        A = []
        path = []
        for i in range(MAXV):
            A.append([0] * MAXV)
            path.append([0] * MAXV)

        def Dispath():
            print("最短路径长度为{}".format(A[1][0]))
            start = path[1][0]
            p = [0]
            while start != 1:
                p.append(start)
                a = start
                start = path[1][a]
            p.append(1)
            p.reverse()
            print("1到0的最短路径为{}".format(p))

        def floyd():
            for i in range(g.n):
                for j in range(g.n):
                    A[i][j] = g.edges[i][j]
                    if i != j and g.edges[i][j] < INF:
                        path[i][j] = i
                    else:
                        path[i][j] = -1
            for k in range(g.n):
                for i in range(g.n):
                    for j in range(g.n):
                        if A[i][j] > A[i][k] + A[k][j]:
                            A[i][j] = A[i][k] + A[k][j]
                            path[i][j] = path[k][j]
            Dispath()

        floyd()


if __name__ == '__main__':
    s = Floyd()
