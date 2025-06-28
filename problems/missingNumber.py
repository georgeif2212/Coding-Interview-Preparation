def missingNumber(nums):
    res = len(nums)

    for i in range(len(nums)):
        res = res + i - nums[i]
        print(res, nums[i], i)

    return res


arr = [1, 2, 3]
print(missingNumber(arr))
