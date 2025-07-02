def reverseInteger(num, acc=0):
    if num == 0:
        return acc

    last_digit = num % 10
    rest = num // 10
    acc = acc * 10 + last_digit

    return reverseInteger(rest, acc)


print(reverseInteger(123))
