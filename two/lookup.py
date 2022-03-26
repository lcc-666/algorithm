def BinSearch(a, low, high, k):
    if low <= high:
        mid = (low + high) // 2
        if a[mid] == k:
            return mid
        if a[mid] > k:
            return BinSearch(a, low, mid - 1, k)
        else:
            return BinSearch(a, mid + 1, high, k)
    else:
        return -1


if __name__ == '__main__':
    a = [5, 6, 3, 1, 7, 9, 4]
    a.sort()
    index = BinSearch(a, 0, len(a) - 1, 3)
    print(index)
