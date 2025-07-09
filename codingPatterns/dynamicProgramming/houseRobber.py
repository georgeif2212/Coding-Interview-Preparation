def houseRobber(nums):
    def _houseRobber(i, memo=None):
        if memo is None:
            memo = {}
        if i >= len(nums):
            return 0
        if i in memo:
            return memo[i]

        memo[i] = max(_houseRobber(i + 1), nums[i] + _houseRobber(i + 2))
        return memo[i]

    return _houseRobber(0)


nums = [2, 7, 9, 3, 1]
# [2, 7, 9, 3, 1]
#
print(houseRobber(nums))


def houseRobber_O1(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev2 = nums[0]              # dp[i-2]
    prev1 = max(nums[0], nums[1])  # dp[i-1]

    for i in range(2, len(nums)):
        curr = max(prev1, nums[i] + prev2)
        prev2 = prev1
        prev1 = curr

    return prev1

nums = [2, 7, 9, 3, 1]
# [2, 7, 9, 3, 1]
#
print(houseRobber_O1(nums))
