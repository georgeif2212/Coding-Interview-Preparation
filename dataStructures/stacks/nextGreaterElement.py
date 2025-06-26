def nextGreaterElement(nums):
    stack = []
    res = [-1] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        while stack and nums[i] >= stack[-1]:
            stack.pop()
        if stack:
            res[i] = stack[-1]

        stack.append(nums[i])
    return res


nums = [2, 1, 2, 4, 3]
print(nextGreaterElement(nums))


# [2, 1, 2, 4, 3]
#              i
# res=[-1,-1,-1,-1,-1],s= [],
# [2, 1, 2, 4, 3]
#              i
# res=[-1,-1,-1,-1,-1],s=[3],
# [2, 1, 2, 4, 3]
#           i
# res=[-1,-1,-1,-1,-1],s= [4],
# [2, 1, 2, 4, 3]
#        i
# res=[-1,-1, 4,-1,-1],s= [2,4],
# [2, 1, 2, 4, 3]
#     i
# res=[-1, 2, 4,-1,-1],s= [1,2,4]
# [2, 1, 2, 4, 3]
#  i
# res=[4, 2, 4,-1,-1],s= [4]
