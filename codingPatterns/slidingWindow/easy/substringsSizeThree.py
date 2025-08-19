def countGoodSubstrings(s):
    counter = 0
    i = 0
    j = 1
    for k in range(2, len(s)):
        if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
            print(i, s[i], j, s[j], k, s[k])
            counter += 1
        i += 1
        j += 1
    return counter


s = "xyzzaz"
print(countGoodSubstrings(s))
