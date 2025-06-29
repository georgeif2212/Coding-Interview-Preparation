def reverse_array(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left >= right:
        return

    # Intercambio
    arr[left], arr[right] = arr[right], arr[left]

    # Llamada recursiva
    reverse_array(arr, left + 1, right - 1)


arr = [1, 2, 3, 4]
reverse_array(arr)
print(arr)  
