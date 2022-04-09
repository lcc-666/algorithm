for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(0, 10):
                for e in range(0, 10):
                    if len({a, b, c, d, e}) != 5:
                        continue
                    else:
                        m = a * 1000 + b * 100 + c * 10 + d
                        n = a * 1000 + b * 100 + e * 10 + d
                        s = e * 10000 + d * 1000 + c * 100 + a * 10 + d
                        if m + n == s:
                            print(a, b, c, d, e)
