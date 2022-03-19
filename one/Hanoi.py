# 递归
def move(n, x, z):
    print("将第{}个盘片从{}移动到{}".format(n, x, z))


def Hanoi(n, x, y, z):
    if n == 1:
        print("将第{}个盘片从{}移动到{}".format(n, x, z))
    else:
        Hanoi(n - 1, x, z, y)
        move(n, x, z)
        Hanoi(n - 1, y, x, z)


# 非递归
class node:
    def __init__(self):
        self.n = 0
        self.x = None
        self.y = None
        self.z = None
        self.tag = 0


def Hanoi1(n, x, y, z):
    st = []
    e = node()
    e.n = n
    e.x = x
    e.y = y
    e.z = z
    e.tag = 1
    st.append(e)

    while st:
        if st[-1].tag == 1:
            e = st[-1]
            st.pop()
            e1 = node()
            e1.n = e.n - 1
            e1.x = e.y
            e1.y = e.x
            e1.z = e.z
            if e1.n == 1:
                e1.tag = 0
            else:
                e1.tag = 1
            st.append(e1)

            e2 = node()
            e2.n = st[-1].n
            e2.x = e.x
            e2.y = e.y
            e2.z = e.z
            e2.tag = 0
            st.append(e2)

            e = st[-1]
            e3 = node()
            e3.n = e.n
            e3.x = e.x
            e3.y = e.z
            e3.z = e.y
            if e3.n == 1:
                e3.tag = 0
            else:
                e3.tag = 1
            st.append(e3)
        elif st[-1].tag == 0:
            print("将1个盘片从{}移动到{}".format(st[-1].x, st[-1].z))
            st.pop()


if __name__ == '__main__':
    Hanoi(3, "x", "y", "z")
    print()
    Hanoi1(3, "x", "y", "z")
