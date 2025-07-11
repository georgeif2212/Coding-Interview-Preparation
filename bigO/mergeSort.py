def merge_sort(arr):
    # Caso base: si el arreglo tiene 0 o 1 elementos, ya está ordenado
    if len(arr) <= 1:
        return arr
    # Paso 1: dividir el arreglo a la mitad
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # ordenar recursivamente la mitad izquierda
    right = merge_sort(arr[mid:])  # ordenar recursivamente la mitad derecha

    # Paso 2: combinar las dos mitades ordenadas
    merged = []
    i = 0  # puntero para left
    j = 0  # puntero para right
    print(left)
    # Paso 3: mezclar elementos en orden
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Agregar lo que sobre en left (si queda algo)
    while i < len(left):
        merged.append(left[i])
        i += 1

    # Agregar lo que sobre en right (si queda algo)
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


nums = [3, 6, 1, 8, 0, 5]
print(nums)
print(merge_sort(nums))
