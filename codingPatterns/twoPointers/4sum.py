def fourSum(nums, result):
    nums.sort()
    res = []
    for i in range(len(nums)):
        j = i + 1
        k = len(nums) - 1
        h = k - 1
        while j < k:
            total = nums[i] + nums[j] + nums[k] + nums[h]
            if total < result:
                j += 1
            elif total > result:
                k -= 1
            else:
                res.append([nums[i], nums[j], nums[k], nums[h]])
                j += 1
                k -= 1

    return res


def fourSum(nums, result):
    nums.sort()
    res = []
    n = len(nums)

    for i in range(n - 3):  # Primer puntero
        if i > 0 and nums[i] == nums[i - 1]:  # Evitar duplicados
            continue
        for j in range(i + 1, n - 2):  # Segundo puntero
            if j > i + 1 and nums[j] == nums[j - 1]:  # Evitar duplicados
                continue
            k, h = j + 1, n - 1  # Tercer y cuarto puntero
            while k < h:
                total = nums[i] + nums[j] + nums[k] + nums[h]
                if total < result:
                    k += 1
                elif total > result:
                    h -= 1
                else:
                    res.append([nums[i], nums[j], nums[k], nums[h]])
                    k += 1
                    h -= 1
                    # Evitar duplicados en `k` y `h`
                    while k < h and nums[k] == nums[k - 1]:
                        k += 1
                    while k < h and nums[h] == nums[h + 1]:
                        h -= 1

    return res


x = fourSum([10, 20, 30, 40, 1, 2], 62)
print(x)  # Expected output: [[1, 10, 20, 31]]


x = fourSum([10, 20, 30, 40, 1, 2], 62)
print(x)  # Expected output:

# [1, 2, 10, 20, 30, 40]
# [1, 2, 10, 20, 30, 40]
#  i  j           k   h   73
# [1, 2, 10, 20, 30, 40]
#  i      j       k   h   81
# [1, 2, 10, 20, 30, 40]
#  i          j   k   h   91

# 62
# [1, 2, 10, 20, 30, 40]
#  i  j           k   h   73
# [1, 2, 10, 20, 30, 40]
#  i  j       k       h   63
# [1, 2, 10, 20, 30, 40]
#  i  j   k           h   53
