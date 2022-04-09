def bubble(a):
    n = len(a)
    for i in range(0, n - 1):
        exchange = False
        for j in range(n - 1, i, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
                exchange = True
        if not exchange:
            return


if __name__ == '__main__':
    num = [7, 5, 9, 8, 4, 6, 3, 2, 1]
    bubble(num)
    print(num)
