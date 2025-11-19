class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued: {item}")
    
    def dequeue(self):
        if not self.is_empty():
            item = self.items.pop(0)
            print(f"Dequeued: {item}")
            return item
        else:
            print("Queue is empty!")
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def display(self):
        print(f"Queue: {self.items}")

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()

print(f"Front element: {queue.front()}")

queue.dequeue()
queue.dequeue()
queue.display()
