for m in range(2, 1000):
    s = 0
    for i in range(1, m // 2+1):
        if m % i == 0:
            s += i


    if m == s:
        print(m)
