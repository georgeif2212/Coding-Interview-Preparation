class Solution:
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                element1 = stack.pop()
                element2 = stack.pop()
                if token == "+":
                    result = element2 + element1
                elif token == "-":
                    result = element2 - element1
                elif token == "*":
                    result = element2 * element1
                elif token == "/":
                    result = int(element2 / element1)  # truncamiento hacia 0
                stack.append(result)
            else:
                # Convertir el número y guardarlo en la pila
                element = int(token)
                stack.append(element)
        return stack[0]  # resultado final


tokens = ["2", "1", "+", "3", "*"]
s = Solution()
print(s.evalRPN(tokens))
