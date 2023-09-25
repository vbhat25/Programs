class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,element):
        self.queue.append(element)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return ("Error")
    
    def is_empty(self):
        return len(self.queue) == 0
    
q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

dequeued_element1 = q.dequeue()
dequeued_element2 = q.dequeue()
dequeued_element3 = q.dequeue()
print(f"Dequeued element: {dequeued_element1},{dequeued_element2},{dequeued_element3}")
print(f"empty queue {q.is_empty()}")