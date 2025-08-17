class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        def isEnglishLetter(char):
            return char.isalpha()

        stringArray = list(s)
        i = 0
        j = len(stringArray) - 1

        while i < j:
            while not isEnglishLetter(stringArray[i]) and i < j:
                i += 1
            while not isEnglishLetter(stringArray[j]) and i < j:
                j -= 1

            stringArray[i], stringArray[j] = stringArray[j], stringArray[i]
            i += 1
            j -= 1
        return "".join(stringArray)


# -..-a
#     i
