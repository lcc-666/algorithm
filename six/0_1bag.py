class NodeType:
    def __init__(self):
        self.w = 0
        self.v = 0
        self.p = 0.0


class bag:
    def __init__(self):
        n = 5
        W = 100
        A = [[10, 20], [20, 30], [30, 66], [40, 40], [50, 60]]
        A.sort(key=lambda x: x[-1]/x[0], reverse=True)
        A.insert(0, [0,0])
        x = [0] * 20

        def Knap():
            v = 0
            weight = W
            i = 1
            while A[i][0] < weight:
                x[i] = 1
                weight -= A[i][0]
                v += A[i][1]
                i += 1

            if weight > 0:
                x[i] = weight / A[i][0]
                v += x[i] * A[i][1]
        def main():
            Knap()
            value=0
            for j in range(1,n+1):
                print(x[j],end=" ")
                value+=x[j]*A[j][1]
            print("\n最大价值{}".format(value))
        main()


if __name__ == '__main__':
    s = bag()
