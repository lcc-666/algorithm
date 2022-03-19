# 递归
import copy
def fac(n):
    if n==1:
        return n
    return n*fac(n-1)
#非递归

class node():
    def __init__(self):
        self.n=0
        self.f=0
        self.tag=0
def fac2(n):
    st=[]
    e=node()
    e2=node()
    e.n=n
    e.tag=1
    st.append(e)
    while st:
        if st[-1].tag==1:
            if st[-1].n==1:
                st[-1].f=1
                st[-1].tag=0
            else:
                e1 = node()
                e1.n=st[-1].n-1
                e1.tag=1
                st.append(e1)
        else:
            e2=st[-1]
            st.pop()
            st[-1].f=st[-1].n*e2.f
            st[-1].tag=0
        if len(st)==1 and st[-1].tag==0:
            break
    return st[-1].f

if __name__ == '__main__':
    s=fac(5)
    a=fac2(5)
    print(s,a)
