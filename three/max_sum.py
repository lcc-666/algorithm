def maxSubSum3(a):
    n = len(a)
    thisSum = 0
    maxSum = 0
    for j in range(n):
        thisSum += a[j]
        if thisSum < 0:
            thisSum = 0
        if maxSum < thisSum:
            maxSum = thisSum
    return maxSum


if __name__ == '__main__':
    a = [-6, 2, 4, -7, 5, 3, 2, -1, 6, -9, 10, -2]
    max = maxSubSum3(a)
    print(max)
