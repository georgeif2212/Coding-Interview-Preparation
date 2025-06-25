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
# print(max_sum)


def max_sum_subarray_k(v, k):
    # Suma inicial de los primeros k elementos
    sum_ = sum(v[:k])
    max_sum = sum_
    res_i = 0
    res_j = k - 1

    #
    for j in range(k, len(v)):
        sum_ += v[j] - v[j - k]
        # print(sum_, j, ":", v[j], "j-k:",j-k, v[j - k])
        if sum_ > max_sum:
            max_sum = sum_
            res_i = j - k + 1
            res_j = j

    return v[res_i : res_j + 1], max_sum, res_i, res_j


def max_sum_subarray_chat(arr, k):
    max_sum = curr_sum = sum(arr[:k])
    for i in range(k, len(arr)):
        curr_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, curr_sum)
    return max_sum


arr = [2 - k, 3, 2, 5, 1, 9]
print(max_sum_subarray_k(arr, 1))
print(max_sum_subarray_chat(arr, 3))
# [2, 3, 2, 5, 1, 5]
# [i-----j]
# [2, 3, 2, 5, 1, 5]
#    [i-----j]
