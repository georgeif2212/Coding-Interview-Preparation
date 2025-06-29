def recursivePalindrome(string, left=0, right=None):
    if right is None:
        right = len(string) - 1

    if left >= right:
        return True

    if string[left] != string[right]:
        return False

    return recursivePalindrome(string, left + 1, right - 1)


print(recursivePalindrome("reconocer"))
