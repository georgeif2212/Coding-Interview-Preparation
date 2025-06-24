def isIsomorphic(s: str, t: str) -> bool:
    char_index_s = {}
    char_index_t = {}
    for i in range(len(s)):
        if s[i] not in char_index_s:
            char_index_s[s[i]] = i
        if t[i] not in char_index_t:
            char_index_t[t[i]] = i

        print(
            char_index_s,
            char_index_s[s[i]],
            "|",
            char_index_t,
            char_index_t[t[i]],
            "|",
        )
        if char_index_s[s[i]] != char_index_t[t[i]]:
            return False

    return True


s = "egg"
t = "adb"
print(isIsomorphic(s, t))
for c1, c2 in zip(s, t):
    print(c1, c2)
