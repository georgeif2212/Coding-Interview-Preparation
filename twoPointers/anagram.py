def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counter = {}

    for char in s:
        counter[char] = counter.get(char, 0) + 1

    print(counter)

    for char in t:
        if char not in counter or counter[char] == 0:
            return False
        counter[char] -= 1

    return True


print(isAnagram("asrgac", "cragsa"))
