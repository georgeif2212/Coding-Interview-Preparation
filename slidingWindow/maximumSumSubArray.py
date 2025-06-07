def maximumSubarraySum(nums, k):
    n = len(nums)
    elements = set()
    current_sum = 0
    max_sum = 0
    begin = 0

    for end in range(n):
        if nums[end] not in elements:
            current_sum += nums[end]
            elements.add(nums[end])

            if end - begin + 1 == k:
                if current_sum > max_sum:
                    max_sum = current_sum

                current_sum -= nums[begin]
                elements.remove(nums[begin])
                begin += 1
        else:
            while nums[begin] != nums[end]:
                current_sum -= nums[begin]
                elements.remove(nums[begin])
                begin += 1

            begin += 1

    return max_sum


# [2, 1, 5, 1, 3, 2] elements:{} cuSum: maxSum: begin:
# [2, 1, 5, 1, 3, 2] elements:{2} cuSum:2 maxSum: begin:


arr = [2, 1, 5, 1, 3, 2]
k = 3
max_sum = maximumSubarraySum(arr, k)
print(max_sum)
