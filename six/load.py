class ship:
    def __init__(self):
        w = [0, 5, 2, 6, 4, 3]
        n = 5
        W = 10
        x = [0] * 6

        def solve():
            w.sort()
            maxw = 0
            restw = W
            for i in range(1,n+1):
                if w[i]<=restw:
                    x[i]=1
                    restw-=w[i]
                    maxw+=w[i]
            return maxw

        maxw=solve()
        print("最优方案")
        for i in range(len(x)):
            if x[i]!=0:
                print("选取重量为{}的集装箱".format(i+1))
        print("总重量={}".format(maxw))


if __name__ == '__main__':
    s = ship()
