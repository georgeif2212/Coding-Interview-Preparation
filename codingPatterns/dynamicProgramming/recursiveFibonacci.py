def fib_memo(n, memo={}):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def fib_bottom_up(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    print(dp)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def fib_bottom_upO1(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        print(a, b)
        a, b = b, a + b
    return b


print(fib_memo(6))
# print(fib_bottom_up(6))
print(fib_bottom_upO1(6))
