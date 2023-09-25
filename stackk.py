class stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Error: Stack is empty"
    
    def is_empty(Self):
        return len(Self.stack) == 0
    
stk = stack()

stk.push(5)
stk.push(10)
stk.push(15)

popped_element = stk.pop()
print(f"Popped element: {popped_element} ")

print(f"The stack is empty {stk.is_empty()}")