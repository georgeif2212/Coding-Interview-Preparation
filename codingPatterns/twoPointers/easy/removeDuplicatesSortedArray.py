def removeDuplicates(nums):
    i = 1
    for j in range(1, len(nums)):
        if nums[j] != nums[i - 1]:
            nums[i] = nums[j]
            i += 1
    return i


x = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
removeDuplicates(x)

# [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
#     i
