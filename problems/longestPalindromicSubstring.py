def longestPalindromicSubstring(s: str) -> str:
    if not s:
        return ""
    
    start, end = 0, 0
    
    for i in range(len(s)):
        len1 = expandAroundCenter(s, i, i)   # Odd length palindromes
        len2 = expandAroundCenter(s, i, i + 1)  # Even length palindromes
        max_len = max(len1, len2)
        
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
            
    return s[start:end + 1]