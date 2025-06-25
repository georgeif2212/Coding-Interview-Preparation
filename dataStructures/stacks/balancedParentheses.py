def is_valid(s):
    stack = []
    mapping = {")": "(",
            "]": "[",
            "}": "{"}

    for char in s:
        print(stack)
        if char in mapping:
            # print(char)
            top = stack.pop() if stack else "#"
            print("char:",char,"| top: ",top)
            if mapping[char] != top:
                return False
        else:
            # print("else: ",char)
            stack.append(char)

    return not stack

# print(is_valid("()"))         # True
# print(is_valid("()[]{}"))     # True
# print(is_valid("(]"))         # False
print(is_valid("([)]"))       # False
# print(is_valid("{[]}"))       # True
# print(is_valid("["))          # False
# print(is_valid("]"))          # False
# print(is_valid(""))           # True

