def maximumLengthSubstring(s):
    charCount = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
        charCount[s[right]] = charCount.get(s[right], 0) + 1

        while charCount.get(s[right], 0) > 2:
            charCount[s[left]] -= 1
            left += 1
        print(left, right)

        max_len = max(max_len, right - left + 1)

    print(charCount)


s = "bcbbbcba"
maximumLengthSubstring(s)
