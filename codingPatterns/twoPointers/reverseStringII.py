class Solution(object):
    def reverseStr(self, s, k):
        n = len(s)  # 1
        s = list(s)  # 2

        for i in range(0, n, 2 * k):  # 3
            s[i : i + k] = reversed(s[i : i + k])  # 4

        return "".join(s)  # 5
