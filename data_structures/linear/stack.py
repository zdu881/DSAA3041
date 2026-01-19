"""
Data Structure: Stack
Description: Basic implementation of a stack using list
Operations: push(), pop(), peek(), isEmpty() - all O(1)
"""

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add an item to the top of the stack"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top item"""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        """Return the top item without removing it"""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]
    
    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the stack"""
        return len(self.items)
    
    def __str__(self):
        return f"Stack({self.items})"

def main():
    # Test the stack implementation
    stack = Stack()
    
    print("Pushing 1, 2, 3 to stack")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    
    print(f"Top element: {stack.peek()}")
    print(f"Stack size: {stack.size()}")
    
    print(f"Popped: {stack.pop()}")
    print(f"After pop: {stack}")
    
    print(f"Is empty? {stack.is_empty()}")

if __name__ == "__main__":
    main()
