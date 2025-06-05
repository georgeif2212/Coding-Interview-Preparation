def lengthOfLongestSubstring(s: str) -> int:
    n = len(s) # Get the length of the string
    maxLength = 0  # Initialize the maximum length of substring
    charMap = {} # Dictionary to store the last index of each character
    left = 0 # Left pointer for the sliding window

    for right in range(n): # Iterate through the string with a right pointer
        if s[right] not in charMap or charMap[s[right]] < left: # Check if the character is not in the map or is outside the current window
            charMap[s[right]] = right # Update the last index of the character
            maxLength = max(maxLength, right - left + 1) # Update the maximum length if the current window is larger
        else: # If the character is already in the map and within the current window
            left = charMap[s[right]] + 1 # Move the left pointer to the right of the last occurrence of the character
            charMap[s[right]] = right # Update the last index of the character

    return maxLength


def lengthOfLongestSubstringTwo(s) :
    left = max_length = 0 # Initialize left pointer and maximum length
    char_set = set() # Set to store characters in the current substring

    for right in range(len(s)): 
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length



# Example usage
s = "abcdabcdebb"
print(lengthOfLongestSubstring(s))  # Output: 3
print(lengthOfLongestSubstringTwo(s))  # Output: 3