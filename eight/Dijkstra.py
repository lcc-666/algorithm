class MGraph:
    def __init__(self):
        INF = float('inf')
        self.n = 7
        self.edges = [[0, 6, INF, INF, INF, 1, INF],
                      [6, 0, 4, INF, INF, INF, 3],
                      [INF, 4, 0, 2, INF, INF, INF],
                      [INF, INF, 2, 0, 6, INF, 5],
                      [INF, INF, INF, 6, 0, 8, 7],
                      [1, INF, INF, INF, 8, 0, INF],
                      [INF, 3, INF, 5, 7, INF, 0]]

class dilkstra:
    def __init__(self):
        INF = float('inf')
        g = MGraph()
        MAXV = 7
        dist = []
        path = []
        S=[]
        for i in range(MAXV):
            dist.append([0] * MAXV)
            path.append([0] * MAXV)
            S.append([0]*MAXV)

        def Dispath(v):
            for i in range(len(dist)):
                print("从0到{}的最短路径为{}".format(i,dist[i]))
        def Dijkstra(v):
            for i in range(g.n):
                dist[i]=g.edges[v][i]
                S[i]=0
                if g.edges[v][i]<INF:
                    path[i]=v
                else:
                    path[i]=-1
            S[v]=1
            path[v]=0
            for i in range(g.n):
                mindis=INF
                for j in range(g.n):
                    if S[j]==0 and dist[j]<mindis:
                        u=j
                        mindis=dist[j]
                S[u]=1
                for j in range(g.n):
                    if S[j]==0:
                        if g.edges[u][i]<INF and dist[u]+g.edges[u][j]<dist[j]:
                            dist[j]=dist[u]+g.edges[u][j]
                            path[j]=u
            Dispath(v)
        Dijkstra(0)

if __name__ == '__main__':
    s=dilkstra()