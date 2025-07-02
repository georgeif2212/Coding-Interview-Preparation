def isSorted(nums, i=0):
    if i == len(nums) - 1:
        return True
    if nums[i] > nums[i + 1]:
        return False

    return isSorted(nums, i + 1)


print(isSorted([1, 3, 5, 6, 7]))
