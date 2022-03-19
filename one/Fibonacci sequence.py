# 斐波那契数列
def Fibonacci(n):
    if n == 1:
        return n
    if n == 2:
        return n

    return Fibonacci(n - 2) + Fibonacci(n - 1)


if __name__ == '__main__':
    a = Fibonacci(5)
    print(a)
