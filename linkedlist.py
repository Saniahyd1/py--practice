class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()
# ---- Driver Code ----
if __name__ == "__main__":
    linked_list = LinkedList()
    elements = list(map(int, input("Enter numbers separated by space: ").split()))
    
    for elem in elements:
        linked_list.append(elem)
    
    print("Linked List:", end=' ')
    linked_list.print_list()
#--delete the node at a given position--
def delete_node(head, position):
    if head is None:
        return head

    temp = head

    if position == 0:
        head = temp.next
        temp = None
        return head

    for i in range(position - 1):
        temp = temp.next
        if temp is None:
            break

    if temp is None or temp.next is None:
        return head

    next = temp.next.next
    temp.next = None
    temp.next = next

    return head
#---delete by value---
def delete_node_by_value(head, key):
    temp = head
    prev = None

    if temp is not None and temp.data == key:
        head = temp.next
        temp = None
        return head

    while temp is not None and temp.data != key:
        prev = temp
        temp = temp.next

    if temp is None:
        return head

    prev.next = temp.next
    temp = None

    return head
#serach for an element in the linked list
