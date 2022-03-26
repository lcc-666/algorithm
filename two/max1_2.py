class max_1_2:
    def __init__(self, a):

        def solve(low, high, max1, max2):
            if low == high:
                max1[0] = a[low]
                max2[0] = -1
            elif low == high - 1:
                max1[0] = max(a[low], a[high])
                max2[0] = min(a[low], a[high])
            else:
                mid = (low + high) // 2
                lmax1 = [0]
                lmax2 = [0]
                solve(low, mid, lmax1, lmax2)
                rmax1 = [0]
                rmax2 = [0]
                solve(mid + 1, high, rmax1, rmax2)

                if lmax1[0] > rmax1[0]:
                    max1[0] = lmax1[0]
                    max2[0] = max(lmax2[0], rmax1[0])
                else:
                    max1[0] = rmax1[0]
                    max2[0] = max(lmax1[0], rmax2[0])

        max1 = [0]
        max2 = [0]
        solve(0, len(a) - 1, max1, max2)
        print("最大值{}，次大值{}".format(max1[0], max2[0]))


if __name__ == '__main__':
    a = [5, 2, 1, 4, 3]
    max_1_2(a)
