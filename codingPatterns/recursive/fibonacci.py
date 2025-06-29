def recursiveFibonacci(n):
    if n <= 1:
        return n
    return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2)

# Llama a la función para n=5
print("Resultado final:", recursiveFibonacci(5))

# print(recursiveFibonacci(8))


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# 0, 1, 2, 3, 4, 5, 6, 7,  8,  9
