class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)
        return f"Pushed {x}"

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def empty(self):
        return not self.data

    def __str__(self):
        return f"Pila (base → cima): {self.data}"


s = Stack()
print(s.empty())
print(s.push(2))
print(s.top())
print(s.push(9))
print(s.push(3))
print(s.empty())
print(s)
