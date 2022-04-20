from queue import Queue


class NodeType:
    def __init__(self):
        self.no = 1
        self.i = 0
        self.w = 0
        self.v = 0
        self.x = [0] * 20
        self.ub = 0.0


class bag:
    def __init__(self):
        n = 3
        W = 30
        w = [0, 16, 15, 15]
        v = [0, 45, 25, 25]
        maxv = [-9999]
        bestx = [0] * 20
        total = [1]

        def bound(e: NodeType):
            i = e.i + 1
            sumw = e.w
            sumv = e.v
            while i <= n and sumw + w[i] <= W:
                sumw += w[i]
                sumv += v[i]
                i += 1
            if i <= n:
                e.ub = sumv + (W - sumw) * (v[i] / w[i])
            else:
                e.ub = sumv

        def EnQueue(e: NodeType, qu: Queue):
            if e.i == n:
                if e.v > maxv[0]:
                    maxv[0] = e.v
                    for j in range(1, n + 1):
                        bestx[j] = e.x[j]
            else:
                qu.put(e)

        def bfs():
            e= NodeType()
            qu = Queue()
            e.i = 0
            e.w = 0
            e.v = 0
            e.no = total[0]
            total[0] += 1
            bound(e)
            qu.put(e)
            while bool(1-qu.empty()):
                e = qu.get()
                if e.w + w[e.i + 1] <= W:
                    e1=NodeType()
                    e1.no = total[0]
                    total[0] += 1
                    e1.i = e.i + 1
                    e1.w = e.w + w[e1.i]
                    e1.v = e.v + v[e1.i]
                    for j in range(1, n + 1):
                        e1.x[j] = e.x[j]
                    e1.x[e1.i] = 1
                    bound(e1)
                    EnQueue(e1, qu)

                e2=NodeType()
                e2.no = total[0]
                total[0] += 1
                e2.i = e.i + 1
                e2.w = e.w
                e2.v = e.v
                for j in range(1, n + 1):
                    e2.x[j] = e.x[j]
                e2.x[e2.i] = 0
                bound(e2)
                if e2.ub > maxv[0]:
                    EnQueue(e2, qu)

        bfs()
        print("分枝限界法求解0/1背包问题:")
        for i in range(1, n + 1):
            print(bestx[i],end=" ")
        print("\n装入总价值为{}".format(maxv[0]))



if __name__ == '__main__':
    s = bag()
