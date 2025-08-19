def findMaxAverage(nums, k):
    n = len(nums)

    suma = sum(nums[:k])
    maxSum = suma

    for i in range(k, n):
        suma = suma - nums[i - k]
        suma = suma + nums[i]
        maxSum = max(maxSum, suma)

    return maxSum / k


#       0  1    2   3  4   5
nums = [1, 12, -5, -6, 50, 3]
k = 4

print(findMaxAverage(nums, k))
