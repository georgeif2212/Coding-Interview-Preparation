# def longestSubstring(s):
#     longest = 0
#     counter = 0
#     i = 0
#     j = 1
#     while j < len(s):
#         if s[i] == s[j]:
#             counter = j - i
#             longest = max(longest, counter)
#             i += 1
#             j = i + 1
#         else:
#             j += 1

#     return longest


# longest = longestSubstring("abcdabcbb")
# print(longest)


def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        # Si el carácter ya está en el set, quita desde la izquierda hasta que ya no esté
        while s[right] in char_set:
            print("REMOVE: ", s[left])
            char_set.remove(s[left])
            left += 1
        # Añade el nuevo carácter
        char_set.add(s[right])
        print(char_set)
        print("current-length:", right - left + 1)
        # Calcula el tamaño actual de la ventana
        max_len = max(max_len, right - left + 1)

    return max_len


# set(a),max
#  0 1 2 3 4 5 6 7
# "a b c a b c b b"
# lr
# set(a,b), max=2
# "a b c a b c b b"
# l  r
# set(a,b,c), max=3
# "a b c a b c b b"
# l    r
# set(a,b,c), max=3
# "a b c a b c b b"
# l      r
# set(b,c), max=3
# "a b c a b c b b"
#    l   r
# set(b,c), max=3
# "a b c a b c b b"
#      l   r
# set(b,c), max=3
# "a b c a b c b b"
#        l   r
# set(b,c), max=3
# "a b c a b c b b"
#        l     r
# set(b,c), max=3
# "a b c a b c b b"
#          l   r
# set(b,c), max=3
# "a b c a b c b b"
#            l r

# p w w k e w
# i j
s = "abcabcbb"
print(lengthOfLongestSubstring(s))
# Input: s = "abcdabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# a b c a b c b b
# i j
# a b c a b c b b
# i   j
# a b c a b c b b
# i     j
# a b c a b c b b
#   i     j
