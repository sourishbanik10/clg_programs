# Define the Node class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to swap nodes in pairs
def swapPairs(head):
    # Base case: if list is empty or has only one node
    if not head or not head.next:
        return head

    # Nodes to be swapped
    first = head
    second = head.next

    # Swapping
    first.next = swapPairs(second.next)
    second.next = first

    # New head is the second node
    return second

# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" → " if current.next else "\n")
        current = current.next

# Example usage
values = [1, 2, 3, 4, 5]
head = create_linked_list(values)
print("Original list:")
print_linked_list(head)

swapped_head = swapPairs(head)
print("Swapped in pairs:")
print_linked_list(swapped_head)
