def subArrayWhichSumIsEqualToX(nums, x):
    j = 0
    results = []
    suma = 0
    for i in range(len(nums)):
        while j < len(nums) and suma < x:
            suma = suma + nums[j]
            j = j + 1
        if suma == x:
            results.append([i, j - 1])
        suma = suma - nums[i]

    return results


arr = [2, 3, 2, 5, 1, 5, 2]
# [2, 3, 2, 5, 1, 5]
# i,j
# [2, 3, 2, 5, 1, 5]
# i,  j
# [2, 3, 2, 5, 1, 5]
#  i,    j
# [2, 3, 2, 5, 1, 5]
#  i,       j
# [2, 3, 2, 5, 1, 5]
#     i,    j
# [2, 3, 2, 5, 1, 5]subArrayWhichSumIsEqualToX(arr, 8)
#        i, j
# [2, 3, 2, 5, 1, 5]
#        i,    j
print(subArrayWhichSumIsEqualToX(arr, 7))
