# 简单选择排序
class SelectSort:
    def __init__(self, a):
        i = 0
        n = len(a)

        def Sort(a, i):
            if i == n - 1:
                return
            k = a.index(min(a[i:]))
            if k != i:
                a[i], a[k] = a[k], a[i]
            Sort(a, i + 1)

        Sort(a,0)
        print(a)

class BubbleSort:
    def __init__(self,a):
        i=0
        n=len(a)
        def sort(n):
            if i==n-1:
                return
            for j in range(i,n-1):
                if a[j]>a[j+1]:
                    a[j],a[j+1]=a[j+1],a[j]
                else:
                    continue
            sort(n-1)
        sort(n)
        print(a)


if __name__ == '__main__':
    ls = [8, 7, 4, 5, 6, 1]
    print("排序前")
    print(ls)
    print("简单选择排序")
    SelectSort(ls)
    print("冒泡排序")
    BubbleSort(ls)
