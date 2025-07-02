def subsets(nums):
    res = []

    def backtrack(i, path):
        if i == len(nums):
            print(path)
            res.append(path[:])
            return
        backtrack(i + 1, path)  # no elegir nums[i]
        path.append(nums[i])  # sí elegir nums[i]
        backtrack(i + 1, path)
        path.pop()  # deshacer elección

    backtrack(0, [])
    return res


def generate_subsets(nums):
    res = []

    def backtrack(start, path):
        print(f"Llamada: start={start}, path={path}")  # 👀 Ver cada llamada

        # Siempre agregamos una copia del path actual
        res.append(path[:])  # ⚠️ [:] para copiar

        for i in range(start, len(nums)):
            # Elegimos nums[i]
            path.append(nums[i])
            print(f"  Incluyendo {nums[i]} → path ahora: {path}")

            # Recurse con el siguiente índice
            backtrack(i + 1, path)

            # Backtrack: quitamos el último elemento
            print(f"  Quitando {path[-1]} → antes de backtrack")
            path.pop()

    backtrack(0, [])
    return res


nums = [2, 1]
print(subsets(nums))
# print(generate_subsets(nums))
