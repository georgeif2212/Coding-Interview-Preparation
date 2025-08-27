def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i


nums = [3, 2, 4]
target = 6

print(twoSum(nums, target))
