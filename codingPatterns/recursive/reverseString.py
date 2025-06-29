def reverseString(string):
    if not string or len(string) == 1:
        return string[0]

    return reverseString(string[1:]) + string[0]


print(reverseString("hola que pasa a todos"))


def reverseString(string):
    if not string or len(string) == 1:
        return string

    rest_reversed = reverseString(string[1:])
    full_result = rest_reversed + string[0]
    return full_result
