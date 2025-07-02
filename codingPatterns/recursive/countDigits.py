def countDigit(num):
    if num <= 0:
        return 0
    count = 1
    return count + countDigit(num // 10)


print(countDigit(45))
