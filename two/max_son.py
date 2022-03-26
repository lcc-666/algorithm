def maxSubSum4(a, left, right):
    if left == right:
        if a[left] > 0:
            return a[left]
        else:
            return 0

    mid = (left + right) // 2

    maxLeftSum = maxSubSum4(a, left, mid)
    maxRightSum = maxSubSum4(a, mid + 1, right)
    maxLeftBorderSum = 0
    leftBorderSum = 0

    for i in range(mid, left-1, -1):
        leftBorderSum += a[i]
        if leftBorderSum > maxLeftBorderSum:
            maxLeftBorderSum = leftBorderSum

    maxRightBorderSum = 0
    rightBorderSum = 0

    for j in range(mid + 1, right+1):
        rightBorderSum += a[j]
        if rightBorderSum > maxRightBorderSum:
            maxRightBorderSum = rightBorderSum
    return max(maxLeftSum, maxRightSum, maxLeftBorderSum + maxRightBorderSum)


if __name__ == '__main__':
    a = [-2, 11, -4, 13, -5, -2]
    print(maxSubSum4(a, 0, len(a) - 1))
