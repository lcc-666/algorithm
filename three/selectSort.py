def select(a):
    n = len(a)
    for i in range(0, n - 1):
        k = i
        for j in range(i + 1, n):
            if a[j] < a[k]:
                k = j
            if k != i:
                a[i], a[k] = a[k], a[i]


if __name__ == '__main__':
    num = [7, 5, 9, 8, 4, 6, 3, 2, 1]
    select(num)
    print(num)
