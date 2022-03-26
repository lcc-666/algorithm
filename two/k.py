def QuickSelect(a, s, t, k):
    i = s
    j = t
    if s < t:
        tmp = a[s]
        while i != j:
            while j > i and a[j] >= tmp:
                j -= 1
            a[i] = a[j]
            while i < j and a[i] <= tmp:
                i += 1
            a[j] = a[i]
        a[i] = tmp

        if k - 1 == i:
            return a[i]
        elif k - 1 < i:
            return QuickSelect(a, s, i - 1, k)
        else:
            return QuickSelect(a, i + 1, t, k)
    elif s == t and s == k - 1:
        return a[k - 1]


if __name__ == '__main__':
    a = [2, 5, 1, 7, 10, 6, 9, 4, 3, 8]
    for k in range(1, len(a)+1):
        e = QuickSelect(a, 0, len(a) - 1, k)
        print("第{}小的元素是{}".format(k,e))
