def letterCombinations(digits):
    digitToLetters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    res = []
    if not digits:
        return res

    def backtrack(index, path):
        if len(path) == len(digits):
            res.append(path)
            return
        for letter in digitToLetters[digits[index]]:
            backtrack(index + 1, path + letter)

    backtrack(0, "")
    return res


print(letterCombinations("2398"))
