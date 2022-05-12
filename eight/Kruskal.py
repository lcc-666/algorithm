class UFSTree:
    def __init__(self):
        self.data = 0
        self.rank = 0
        self.parent = 0


class Edge:
    def __init__(self):
        self.u = 0
        self.v = 0
        self.w = 0


class MGraph:
    def __init__(self):
        INF = float('inf')
        self.n = 7
        self.edges = [[0, 6, INF, INF, INF, 1, INF],
                      [6, 0, 4, INF, INF, INF, 3],
                      [INF, 4, 2, INF, INF, INF],
                      [INF, INF, 2, 0, 6, INF, 5],
                      [INF, INF, INF, 6, 0, 8, 7],
                      [1, INF, INF, INF, 8, 0, INF],
                      [INF, 3, INF, 5, 7, INF, 0]]


class kruskal:
    def __init__(self):
        INF = float('inf')
        g = MGraph()
        t = []
        E = []
        MaxSize = 20
        for i in range(MaxSize):
            t.append(UFSTree())
            E.append(Edge())

        def MAKE_SET():
            for i in range(g.n):
                t[i].parent = i

        def FIND_SET(x):
            if x != t[x].parent:
                return FIND_SET(t[x].parent)
            else:
                return x

        def UNION(x, y):
            x = FIND_SET(x)
            y = FIND_SET(y)
            if t[x].rank > t[y].rank:
                t[y].parent = x
            else:
                t[x].parent = y
                if t[x].parent == t[y].rank:
                    t[y].rank += 1

        def Kruskal():
            k = 0
            for i in range(g.n):
                for j in range(i):
                    if g.edges[i][j] != 0 and g.edges[i][j] != INF:
                        E[k].u = i
                        E[k].v = j
                        E[k].w = g.edges[i][j]
                        k+=1
            E.sort(key=lambda x: x.w)
            MAKE_SET()
            k = 1
            j = 0
            while k < g.n:
                u1 = E[j].u
                v1 = E[j].v
                sn1 = FIND_SET(u1)
                sn2 = FIND_SET(v1)

                if sn1 != sn2:
                    print("{},{}:{}".format(u1, v1, E[j].w))
                    k += 1
                    UNION(u1, v1)
                j += 1

        Kruskal()
if __name__ == '__main__':
    s=kruskal()
