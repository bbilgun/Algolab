class StackWithBackup:
    def __init__(self):
        self.stack = []
        self.backup = []

    def push(self, x):
        self.stack.append(x)
        if len(self.stack) % 3 == 0:  
            self.backup = self.stack[:]
            print(f"Нөөцлөлт хийгдэв: {self.backup}")

    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()

    def get_stack(self):
        return self.stack

stack = StackWithBackup()
stack.push(1)
stack.push(2)
stack.push(3)  # Нөөцлөлт хийгдэнэ
stack.push(4)
stack.push(5)
stack.push(6)  # Нөөцлөлт хийгдэнэ
stack.pop()
print(stack.get_stack())
