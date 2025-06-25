class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, x):
        self.data.append(x)

    def dequeue(self):
        if self.empty():
            raise IndexError("No se puede hacer dequeue a una cola vacía")
        return self.data.pop(0)

    def front(self):
        if self.empty():
            raise IndexError("La cola está vacía.")
        return self.data[0]

    def empty(self):  # ¿cola vacía?
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def __str__(self):
        return f"Cola (frente → final): {self.data}"


q = Queue()
print(q.empty())  # True

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q)  # Cola (frente → final): [10, 20, 30]
print(q.front())  # 10
print(q.dequeue())  # 10
print(q)  # Cola (frente → final): [20, 30]
print(q.size())  # 2
