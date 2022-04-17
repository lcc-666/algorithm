def fun(op,sum,prevadd,a,i):
    N=len(a)

    if i==N:
        if sum==100:
            print(a[0],end='')
            for j in range(1,N):
                if op[j]!=" ":
                    print(op[j],end='')
                print(a[j],end='')
            print()
        return


    op[i]='+'
    sum+=a[i]
    fun(op,sum,a[i],a,i+1)
    sum-=a[i]

    op[i] = '-'
    sum -= a[i]
    fun(op, sum, -a[i], a, i + 1)
    sum += a[i]

    op[i]=" "
    sum-=prevadd
    if prevadd>0:
        tmp=prevadd*10+a[i]
    else:
        tmp = prevadd * 10 - a[i]
    sum+=tmp
    fun(op,sum,tmp,a,i+1)
    sum-=tmp
    sum+=prevadd

if __name__ == '__main__':
    a=[1,2,3,4,5,6,7,8,9]
    op=[0]*9
    fun(op,a[0],a[0],a,1)
