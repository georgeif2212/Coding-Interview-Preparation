def isAnagram(self, s: str, t: str) -> bool:

    if len(s) != len(t):
        return False
    sMap = {}
    tMap = {}
    for char in s:
        sMap[char] = sMap.get(char, 0) + 1
    for char in t:
        tMap[char] = tMap.get(char, 0) + 1

    return sMap == tMap

    return sorted(s) == sorted(t)
