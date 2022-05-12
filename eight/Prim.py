class MGraph:
    def __init__(self):
        INF = float('inf')
        self.n = 7
        self.edges = [[0, 6, INF, INF, INF, 1, INF],
                      [6, 0, 4, INF, INF, INF, 3],
                      [INF, 4, 0,2, INF, INF, INF],
                      [INF, INF, 2, 0, 6, INF, 5],
                      [INF, INF, INF, 6, 0, 8, 7],
                      [1, INF, INF, INF, 8, 0, INF],
                      [INF, 3, INF, 5, 7, INF, 0]]


class prim:
    def __init__(self):
        g = MGraph()
        INF = float('inf')
        MAXV = 10
        lowcost = []
        closest = []
        for i in range(MAXV):
            lowcost.append(0)
            closest.append(0)

        def prim(v):
            for j in range(g.n):
                lowcost[j] = g.edges[v][j]
                closest[j] = v
            for i in range(1, g.n):
                mincost = INF
                for j in range(0, g.n):
                    if lowcost[j] != 0 and lowcost[j] < mincost:
                        mincost = lowcost[j]
                        k = j
                print("边{}{}权为：{}".format(closest[k], k, mincost))
                lowcost[k] = 0
                for j in range(g.n):
                    if g.edges[k][j] != 0 and g.edges[k][j] < lowcost[j]:
                        lowcost[j] = g.edges[k][j]
                        closest[j] = k

        prim(0)


if __name__ == '__main__':
    s = prim()
