from queue import PriorityQueue


class HTreeNode:
    def __init__(self):
        self.data = ""
        self.weight = 0
        self.parent = -1
        self.lchild = -1
        self.rchild = -1


class NodeType:
    def __init__(self):
        self.no = 0
        self.data = ""
        self.weight = 0


class HT:
    def __init__(self):
        n = 5
        ht = []
        char = ["a", "b", "c", "d", "e"]
        W = [4, 2, 1, 7, 3]
        htcode = {}
        for i in range(5):
            e = HTreeNode()
            e.data = char[i]
            e.weight = W[i]
            ht.append(e)
        for j in range(20):
            ht.append(HTreeNode())


        def CreateHTree():
            qu = PriorityQueue()
            for i in range(n):
                e = NodeType()
                e.no = i
                e.data = ht[i].data
                e.weight = ht[i].weight
                qu.put((e.weight, e))

            for j in range(n, 2 * n - 1):
                e1 = qu.get()[-1]
                e2 = qu.get()[-1]
                ht[j].weight = e1.weight + e2.weight
                ht[j].lchild = e1.no
                ht[j].rchild = e2.no
                ht[e1.no].parent = j
                ht[e2.no].parent = j
                e = NodeType()
                e.no = j
                e.weight = e1.weight + e2.weight
                qu.put((-e.weight, e))

        def CreateHCode():
            for i in range(n):
                code = ""
                curno = i
                f = ht[curno].parent
                while f != -1:
                    if ht[f].lchild == curno:
                        code = "0" + code
                    else:
                        code = "1" + code
                    curno = f
                    f = ht[curno].parent
                htcode[ht[i].data] = code

        CreateHTree()
        CreateHCode()
        for i in htcode:
            print(i,htcode[i],sep=":")


if __name__ == '__main__':
    s = HT()
