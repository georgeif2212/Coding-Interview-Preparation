def twoSum(nums, result):
    res = []
    nums.sort()

    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] + nums[j] < result:
            i += 1
        elif nums[i] + nums[j] > result:
            j -= 1
        else:
            res.append([nums[i], nums[j]])
            i += 1
            j -= 1
    return res


x = twoSum([-1, 0, 1, 2, -1, -4], 10)
print(x)  # Expected output: [[0, 3], [1, 2]]

# [-1, 0, 1, 2, -1, -4]        2
# [-4, -1, -1, 0, 1, 2]        2
#   i                j   -2,   2
#       i            j   -1,   2
#              i     j    2,   2        [3,5]=2


def two_sum_array_not_sorted(nums, target):
    result = []
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            print("SEEN[DIFF]", seen[diff])
            result.append([seen[diff], i])
        seen[num] = i
    print(seen)
    return result



# [-1, 0, 1, 2, -1, -4]
#   0  1  2  3   4   5
x = two_sum_array_not_sorted([-1, -2, 1, 2, -1, -4, 5], 3)
print(x)


# Crear un diccionario
frecuencia = {'a': 2, 'b': 1}
frecuencia['c'] = 3
print(frecuencia['c'])