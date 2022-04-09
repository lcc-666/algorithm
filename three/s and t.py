def count(s, t):
    num = 0
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
        if j == len(t):
            num += 1
            j = 0
    return num


if __name__ == '__main__':
    s = "abababa"
    t = "aba"
    c = count(s, t)
    print(c)
