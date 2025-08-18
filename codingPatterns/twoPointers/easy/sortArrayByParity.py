def sortArrayByParityII(nums):
    evenIndex = 0
    oddIndex = 1
    i = 0
    n = len(nums)
    res = [0] * n
    for i in range(n):
        if nums[i] % 2 == 0:
            res[evenIndex] = nums[i]
            evenIndex += 2
        else:
            res[oddIndex] = nums[i]
            oddIndex += 2

    return res


def sortArrayByParityII(nums):

    n = len(nums)
    i, j = 0, 1  # i apunta a índice par, j a índice impar
    while i < n and j < n:
        if nums[i] % 2 == 0:  # par bien colocado
            i += 2
        elif nums[j] % 2 == 1:  # impar bien colocado
            j += 2
        else:  # par en índice impar y/o impar en índice par
            nums[i], nums[j] = nums[j], nums[i]
            i += 2
            j += 2
    return nums


# [3,2,5,7]
#  i j
# [3,3,5,7]
#  i j
