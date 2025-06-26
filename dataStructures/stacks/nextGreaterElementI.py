#
# * 496 Next Greater Element
# The next greater element of some element x in an array is the first
# greater element that is to the right of x in the same array.
# You are given two distinct 0-indexed integer arrays nums1 and nums2,
# where nums1 is a subset of nums2.
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j]
#  and determine the next greater element of nums2[j] in nums2. If there
# is no next greater element, then the answer for this query is -1.


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        hm = {}

        for i in range(len(nums2) - 1, -1, -1):
            while stack and nums2[i] >= stack[-1]:
                stack.pop()

            hm[nums2[i]] = stack[-1] if stack else -1
            stack.append(nums2[i])

        return [hm[num] for num in nums1]


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

s = Solution()
res = s.nextGreaterElement(nums1, nums2)
print(res)
