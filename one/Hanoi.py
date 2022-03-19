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

def


if __name__ == '__main__':
    Hanoi(2, "x", "y", "z")
