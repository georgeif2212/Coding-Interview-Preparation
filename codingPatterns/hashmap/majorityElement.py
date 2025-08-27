def majorityElement(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    print(freq)
    return max(freq, key=freq.get)


nums = [3, 3, 4]
print(majorityElement(nums))
