class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> " if curr.next else "\n")
            curr = curr.next

    def reverse(self):
        curr = self.head
        temp = None
        while curr:
            # Swap next and prev
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            # Move to next node (which is prev now)
            curr = curr.prev
        # Reset head to the last node processed
        if temp:
            self.head = temp.prev

# 🚀 Create and reverse the list
dll = DoublyLinkedList()
for i in range(1, 6):  # Add nodes with data 1 to 5
    dll.append(i)

print("Original list:")
dll.display()

dll.reverse()

print("Reversed list:")
dll.display()
