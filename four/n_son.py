def dispasolution(a, n, x):
    ans = []
    for i in range(n):
        if x[i] == 1:
            ans.append(a[i])
    print(ans)


def dfs(a, n, i, x):
    if i >= n:
        dispasolution(a, n, x)

    else:
        x[i] = 0
        dfs(a, n, i + 1, x)
        x[i] = 1
        dfs(a, n, i + 1, x)


if __name__ == '__main__':
    a = [1, 2, 3]
    x = [0, 0, 0]
    n = len(a)
    i = 0
    dfs(a, n, i, x)
