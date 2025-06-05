def removeDuplicates(nums):
    nums.sort()
    i = 0
    j = 1
    while j < len(nums):
        if nums[i] == nums[j]:
            nums.pop(j)
        else:
            i += 1
            j = i + 1
    return len(nums)


x = [1, 1, 3, 2, 1, 3]
length = removeDuplicates(x)
print(length)

# Remove Duplicates from Sorted Array
# En un array ordenado, elimina los duplicados in-place y retorna la longitud del nuevo array.

# Input: [1,1,2]

# Output: 2 (nuevo array: [1,2])
# [1,1,3,2,1,3]
# [1,1,1,2,3,3]
# i  j
# [1,1,2,3,3]
# i  j
# [1,2,3,3]
#      i j


def removeDuplicates(nums):
    if not nums:
        return 0

    nums.sort()  # Ordenar la lista
    i = 0  # Índice para elementos únicos

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]  # Mover el elemento único al índice correcto

    print(nums)  # Mostrar el array modificado
    # Recortar la lista para que solo contengaj los elementos únicos
    del nums[i + 1 :]

    return len(nums)  # Retornar la


x = [1, 1, 3, 2, 1, 3]
length = removeDuplicates(x)
print(length)

# [1,1,3,2,1,3]
# [1,1,1,2,3,3]
#  i j
# [1,1,1,2,3,3]
#  i   j
# [1,1,1,2,3,3]
#  i     j
# [1,1,1,2,3,3]
#    i   j
# [1,2,1,2,3,3]
#    i   j
# [1,2,1,2,3,3]
#    i     j
# [1,2,3,2,3,3]
#      i   j
# [1,2,3,2,3,3]
#      i     j
# [1,2,3]
# Remove Duplicates from Sorted Array
# En un array ordenado, elimina los duplicados in-place y retorna la longitud del nuevo array.

# Input: [1,1,2]

# Output: 2 (nuevo array: [1,2])
# [1,1,3,2,1,3]
# [1,1,1,2,3,3]
# i  j
# [1,1,2,3,3]
# i  j
# [1,2,3,3]
#      i j
