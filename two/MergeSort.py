def Merge(a, low, mid, high):
    tmpa = []
    for _ in range(high - low + 1):
        tmpa.append(0)
    i = low
    j = mid + 1
    k = 0
    while i <= mid and j <= high:
        if a[i] <= a[j]:
            tmpa[k] = a[i]
            i += 1
            k += 1
        else:
            tmpa[k] = a[j]
            j += 1
            k += 1
    while i <= mid:
        tmpa[k] = a[i]
        i += 1
        k += 1
    while j <= high:
        tmpa[k] = a[j]
        j += 1
        k += 1
    item = 0
    for h in range(low, high + 1):
        a[h] = tmpa[item]
        item += 1


def MergeSort(a, low, high):
    if low < high:
        mid = (low + high) // 2
        MergeSort(a, low, mid)
        MergeSort(a, mid + 1, high)
        Merge(a, low, mid, high)


if __name__ == '__main__':
    a = [9, 5, 7, 4, 1, 3, 2, 8]
    print("排序前",a)
    MergeSort(a, 0, len(a) - 1)
    print("排序后",a)
