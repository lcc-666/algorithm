class Queens:
    def __init__(self,n):
        q = [0] * 20
        self.count = 0

        def dispasolution(n):
            self.count += 1
            print("第{}个解".format(self.count))
            for i in range(1,n+1):
                print((i, q[i]), end=" ")
            print()

        def place(i):
            j = 1
            if i == 1:
                return True

            while j < i:
                if (q[j] == q[i]) or (abs(q[j] - q[i]) == abs(j - i)):
                    return False
                j += 1
            return True

        i = 1
        q[i] = 0
        while i >= 1:
            q[i] += 1

            while q[i] <= n and bool(1-place(i)):
                q[i] += 1

            if q[i] <= n:
                if i == n:
                    dispasolution(n)
                else:
                    i += 1
                    q[i] = 0
            else:
                i -= 1


if __name__ == '__main__':
    s = Queens(4)
