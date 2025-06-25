class Stack:
    def __init__(self):
        self.data=[]

    def push(self,x):
        self.data.append(x)
    
    def pop(self,x):
        return self.data.pop()

    def top(self,x):
        return self.data[-1]
    
    def empty(self):
        return not self.data