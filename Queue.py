#30.Implement a Queue
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]


# Example usage:

queue = Queue()

while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = input("Enter a value to enqueue: ")
        queue.enqueue(value)
        print("Value", value, "enqueued.")
    elif choice == 2:
        value = queue.dequeue()
        if value is None:
            print("Queue is empty.")
        else:
            print("Dequeued value:", value)
    elif choice == 3:
        value = queue.peek()
        if value is None:
            print("Queue is empty.")
        else:
            print("Front value:", value)
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")

print("Queue operations finished.")