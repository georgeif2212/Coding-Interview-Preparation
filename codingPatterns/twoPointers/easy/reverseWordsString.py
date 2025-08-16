class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        print(s)
        res = ""
        for word in s:
            word = list(word)
            i = 0
            j = len(word) - 1
            while i < j:
                word[i], word[j] = word[j], word[i]
                i += 1
                j -= 1
            res = res + "".join(word) + " "
        return res


class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the input string into words and reverse each word
        words = s.split()
        reversed_words = [word[::-1] for word in words]

        # Join the reversed words to form the final result
        return " ".join(reversed_words)


s = "Let's take LeetCode contest"

sol = Solution()
print(sol.reverseWords(s))

print(s[::-1])