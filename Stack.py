#29.Implement a Stack
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]


# Example usage:

stack = Stack()

while True:
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = input("Enter a value to push: ")
        stack.push(value)
        print("Value", value, "pushed to the stack.")
    elif choice == 2:
        value = stack.pop()
        if value is None:
            print("Stack is empty.")
        else:
            print("Popped value:", value)
    elif choice == 3:
        value = stack.peek()
        if value is None:
            print("Stack is empty.")
        else:
            print("Top value:", value)
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")

print("Stack operations finished.")