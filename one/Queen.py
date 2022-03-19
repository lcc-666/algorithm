# 皇后问题

class Queen:
    def __init__(self, i, n):
        q = [0] * n
        self.count = 0

        def dispasolution(n):
            self.count += 1
            print("第{}个解".format(self.count))
            for i in range(n):
                print((i, q[i]), end=" ")
            print()

        def place(i, j):
            if i == 0:
                return True
            k = 0
            while k < i:
                if q[k] == j or abs(q[k] - j) == abs(i - k):
                    return False
                k += 1
            return True

        def queen(i, n):
            if i > n - 1:
                dispasolution(n)
            else:
                for j in range(n):
                    if place(i, j):
                        q[i] = j
                        queen(i + 1, n)

        queen(i, n)

if __name__ == '__main__':
    s = Queen(0, 6)
    print()
