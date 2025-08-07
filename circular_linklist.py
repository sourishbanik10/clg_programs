class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def is_circular(head):
    if head is None:
        return False

    slow = head
    fast = head.next

    while fast is not None and fast.next is not None:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False

# Creating a circular linked list
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Circular link_list

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1 

print(is_circular(node1))  
