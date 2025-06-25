# 202. Happy Number
# Easy
# Topics
# premium lock icon
# Companies
# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.


def getNext(n):
    sum_ = 0
    while n > 0:
        digit = n % 10
        sum_ += digit * digit
        n = n // 10
    return sum_


def isHappy(n):
    slow = n
    fast = getNext(n)
    while fast != 1 and slow != fast:
        print(slow, fast)
        slow = getNext(slow)
        fast = getNext(getNext(fast))
        print(slow, fast)
    return fast == 1


print(isHappy(19))

# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
