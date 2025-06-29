def countTil0(n):
    if n < 0:
        return
    print(n)
    countTil0(n - 1)


def countFrom0(n):
    if n < 0:
        return
    countFrom0(n - 1)
    print(n)  


print(countTil0(5))

print(countFrom0(5))
