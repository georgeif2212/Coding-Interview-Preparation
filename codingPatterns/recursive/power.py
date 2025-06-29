def power(n, t):
    if t == 0:
        return 1
    return n * power(n, t - 1)


print(power(2, 3))
