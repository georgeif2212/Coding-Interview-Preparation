def combinationSum(candidates, target):
    res = []

    def backtrack(start, path, total):
        print(path)
        if total == target:
            res.append(path[:])
            return
        if total > target:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, total + candidates[i])  # i → reuse allowed
            path.pop()

    backtrack(0, [], 0)
    return res


candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))
