def factorialRecursive(n):
    if n == 1:
        return 1
    return n * factorialRecursive(n - 1)


print(factorialRecursive(6))
# 5 * 4 * 3 * 2 * 1 = 120
