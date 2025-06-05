def reverseString(s):
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

s=['Q','u','e','P','a','s','a','P','E','r','r','o']
reverseString(s)
print(s) 
