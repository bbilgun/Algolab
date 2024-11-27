from collections import deque

class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        
        result = self.queue1.popleft()

        self.queue1, self.queue2 = self.queue2, self.queue1

        return result

    def top(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        result = self.queue1.popleft()
        self.queue2.append(result)  

        self.queue1, self.queue2 = self.queue2, self.queue1

        return result

    def empty(self) -> bool:
        return not self.queue1

obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())    # Output: 2
print(obj.pop())    # Output: 2
print(obj.empty())  # Output: False
