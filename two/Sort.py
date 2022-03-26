

def Partition(a, s, t):
    i = s
    j = t
    tmp = a[s]
    while i != j:
        while j > i and a[j] >= tmp:
            j -= 1
        a[i] = a[j]
        while i < j and a[i] <= tmp:
            i += 1
        a[j] = a[i]
    a[i] = tmp
    return i

def QuickSort(a,s, t):
    if s < t:
        i = Partition(a, s, t)
        QuickSort(a, s, i - 1)
        QuickSort(a, i + 1, t)



if __name__ == '__main__':
    a = [6, 8, 6, 4, 7, 6, 1, 56, 8]
    QuickSort(a,0,len(a)-1)
    print(a)



