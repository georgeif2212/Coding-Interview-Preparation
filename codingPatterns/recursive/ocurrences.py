def count_occur(nums, num):
    if not nums:
        return 0
    if nums[0] == num:
        count = 1
    else:
        count = 0
    return count + count_occur(nums[1:], num)


def count_occur(nums, num, i=0):
    if i == len(nums):
        return 0

    count = 1 if nums[i] == num else 0
    return count + count_occur(nums, num, i + 1)


print(count_occur([1, 2, 3, 2, 2, 5], 2))
