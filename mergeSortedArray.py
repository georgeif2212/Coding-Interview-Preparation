def mergeSortedArray(nums1, nums2, m, n):
    i = m - 1  # nums1's last element index valid number
    j = n - 1  # nums2's last element index
    k = m + n - 1  # nums1's last element index

    while j >= 0:
        if i < 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        elif nums1[i] < nums2[j]:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        elif nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
        else:
            nums1[k]=nums2[j]
            i -= 1
            j -= 1
            k -= 1

    # [1, 2, 7, 0, 0, 0] [2, 5, 6]
    #        i        k         j
    # [1, 2, 7, 0, 0, 7] [2, 5, 6]
    #     i        k            j
    # [1, 2, 7, 0, 6, 7] [2, 5, 6]
    #     i        k            j
    # [1, 2, 7, 0, 6, 7] [2, 5, 6]
    #     i     k            j
    # [1, 2, 7, 5, 6, 7] [2, 5, 6]
    #     i  k            j
    # [1, 2, 2, 5, 6, 7] [2, 5, 6]
    #  i  k            j

    return


nums1 = [1, 2, 7, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
mergeSortedArray(nums1, nums2, m, n)

print(nums1)
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
