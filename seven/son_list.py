class long_list:
    def __init__(self):
        MAX=10
        dp = []
        for i in range(MAX):
            dp.append([0] * MAX)
        subs=[]
        a =["a","b","c","b","d","b"]
        m=len(a)
        b=["a","c","b","b",'a',"b","d","b","b"]
        n=len(b)


        def LCSlength():
            for i in range(1,m+1):
                for j in range(1,n+1):
                    if a[i-1]==b[j-1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = max(dp[i][j - 1],dp[i - 1][j])
        def Buildsubs():
            k=dp[m][n]
            i=m
            j=n
            while k>0:
                if dp[i][j]==dp[i-1][j]:
                    i-=1
                elif dp[i][j]==dp[i][j-1]:
                    j-=1
                else:
                    subs.append(a[i-1])
                    i-=1
                    j-=1
                    k-=1
        LCSlength()
        Buildsubs()
        subs.reverse()
        print("结果LCS={}".format("".join(subs)))
if __name__ == '__main__':
    s=long_list()
                        


        



