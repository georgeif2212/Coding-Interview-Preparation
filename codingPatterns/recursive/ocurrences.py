def count_occur(nums, num):
    if not nums:
        return 0
    if nums[0] == num:
        count = 1
    else:
        count = 0
    return count + count_occur(nums[1:], num)


print(count_occur([1, 2, 3, 2, 2, 5], 2))
