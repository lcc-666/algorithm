from queue import PriorityQueue


class NodeType:
    def __init__(self):
        self.no = 0
        self.i = 0
        self.x = [0] * 5
        self.worker = [False] * 5
        self.cost = 0
        self.lb = 0


class mission:
    def __init__(self):
        n = 4
        c = [[0], [0, 9, 2, 7, 8], [0, 6, 4, 3, 7], [0, 5, 8, 1, 8], [0, 7, 6, 9, 4]]
        bestx = [0] * 5
        total = [1]
        INF = 99999
        mincost = [INF]

        def bound(e: NodeType):
            minsum = 0

            for i1 in range(e.i + 1, n + 1):
                minc = INF
                for j1 in range(1, n + 1):
                    if e.worker[j1] is False and c[i1][j1] < minc:
                        minc = c[i1][j1]
                minsum += minc
            e.lb = e.cost + minsum

        def bfs():
            e = NodeType()
            qu = PriorityQueue()
            bound(e)
            e.no = total[0]
            total[0] += 1
            qu.put((e.lb, e))
            while qu.empty() is False:
                e = qu.get()[-1]
                qu=PriorityQueue()
                if e.i == n:
                    if e.cost < mincost[0]:
                        mincost[0] = e.cost
                        for j in range(1, n + 1):
                            bestx[j] = e.x[j]


                for j in range(1, n + 1):
                    e1 = NodeType()
                    e1.i = e.i + 1
                    if e.worker[j]:
                        continue

                    for i1 in range(1, n + 1):
                        e1.x[i1] = e.x[i1]
                    e1.x[e1.i] = j

                    for i2 in range(1, n + 1):
                        e1.worker[i2] = e.worker[i2]
                    e1.worker[j] = True
                    e1.cost = e.cost + c[e1.i][j]
                    bound(e1)
                    e1.no = total[0]
                    total[0] += 1
                    if e1.lb <= mincost[0]:
                        qu.put((e1.lb, e1))

        bfs()
        for k in range(1, n + 1):
            print("第{}个人分配第{}个任务".format(k, bestx[k]))
        print("总成本是{}".format(mincost[0]))


if __name__ == '__main__':
    s = mission()
