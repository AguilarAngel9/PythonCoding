# Linked list.

# Each node has two entries: a data field and a next field,
# which points to the next node in the list, 
# with the next field of the last node being null.

class ListNode:

    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node # Pointer to the next node. 
        # The last element is always gonna have it's next node as None
    
    # Search for a key
    def search_list(L, key):
        while L and L.data != key:
            L = L.next
        # If the key was not present in the list, L will have become null.
        return L
    
    # Insert a new node after a specified node,.
    def insert_after(node, new_node):
        new_node.next = node.next
        node.next = new_node

    # Delate the node past this one. Assume node is not a tail.
    def delate_after(node):
        node.next = node.next.next
