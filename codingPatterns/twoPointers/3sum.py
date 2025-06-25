def threeSum(nums):
    res = []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = len(nums) - 1

        while j < k:
            total = nums[i] + nums[j] + nums[k]

            if total > 0:
                k -= 1
            elif total < 0:
                j += 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                j += 1

                while nums[j] == nums[j - 1] and j < k:
                    j += 1

    return res

x =  threeSum([-1, 0, 1, 2, -1, -4])
print(x)  # Debería imprimir [[-1, -1, 2], [-1, 0, 1]]  

# [-1, 0, 1, 2, -1, -4]
# [-4, -1, -1, 0, 1, 2]
#  i    j            k =- 3
#  i           j     k =- 2
#  i              j  k =- 1
#  i                 jk =- 1
#      i   j         k = 0
# [-1,-1,2]
# [-4, -1, -1, 0, 1, 2]
#       i      j     k = 1
#       i      j  k    = 0
# [-1,0,1]

def threeSum2(nums):
    res = []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = len(nums) - 1

        while j < k:
            total = nums[i] + nums[j] + nums[k]

            if total > 0:
                k -= 1
            elif total < 0:
                j += 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                j += 1

                while j < k and nums[j] == nums[j - 1]:
                    j += 1

    return res
