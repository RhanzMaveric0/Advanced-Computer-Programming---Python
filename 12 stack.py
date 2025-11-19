class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
        print(f"Pushed: {item}")
    
    def pop(self):
        if not self.is_empty():
            item = self.items.pop()
            print(f"Popped: {item}")
            return item
        else:
            print("Stack is empty!")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def display(self):
        print(f"Stack: {self.items}")

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()

print(f"Top element: {stack.peek()}")

stack.pop()
stack.pop()
stack.display()
