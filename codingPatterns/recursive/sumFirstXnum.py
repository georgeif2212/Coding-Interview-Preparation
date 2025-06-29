def sumFirstNum(n):
    if n == 0:
        return 0
    return n + sumFirstNum(n - 1)


def sumFirstNumExplicit(n):
    if n == 0:
        print(f"sum(0) = 0")
        return 0

    partial = sumFirstNumExplicit(n - 1)  # 1️⃣ primero va hacia abajo
    total = n + partial  # 2️⃣ luego sube con la suma
    print(f"sum({n}) = {total}")  # 3️⃣ imprime al regresar
    return total


print(sumFirstNumExplicit(4))
