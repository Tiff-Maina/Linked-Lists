# Node class represents each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data      # Store the value of the node
        self.next = None      # Pointer to the next node in the list (None by default)


# SinglyLinkedList class manages the entire linked list
class SinglyLinkedList:
    def __init__(self):
        self.head = None      # Head of the list (initially empty)

    # Method to add a new node at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)     # Create a new node with the given data
        if self.head is None:
            self.head = new_node  # If the list is empty, new node becomes the head
            return

        # Traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node   # Link the new node at the end

    # Method to add a new node at the beginning of the list
    def insert_at_start(self, data):
        new_node = Node(data)     # Create a new node
        new_node.next = self.head # Point it to the current head
        self.head = new_node      # Make it the new head

    # Method to insert a node at a specific index
    def insert_at_index(self, index, data):
        if index < 0:
            print("Invalid index")  # Negative index is not allowed
            return

        if index == 0:
            self.insert_at_start(data)  # Insert at start if index is 0
            return

        new_node = Node(data)
        current = self.head
        count = 0

        # Move to the node just before the target index
        while current and count < index - 1:
            current = current.next
            count += 1

        if current is None:
            print("Index out of bounds")  # If index is too large
            return

        new_node.next = current.next   # Link new node to next node
        current.next = new_node        # Link previous node to new node

    # Method to delete a node at a specific index
    def delete_at_index(self, index):
        if index < 0 or self.head is None:
            print("Invalid index or empty list")  # Can't delete if index is invalid or list is empty
            return

        if index == 0:
            self.head = self.head.next  # Remove the head node
            return

        current = self.head
        count = 0

        # Move to the node just before the one to be deleted
        while current.next and count < index - 1:
            current = current.next
            count += 1

        if current.next is None:
            print("Index out of bounds")  # No node exists at that index
            return

        current.next = current.next.next  # Skip the node to delete it

    # Method to search for a value in the list
    def search(self, value):
        current = self.head
        index = 0

        # Traverse the list and check each node's data
        while current:
            if current.data == value:
                return index     # Return the index if value is found
            current = current.next
            index += 1

        return -1  # Value not found

    # Method to print all elements of the linked list
    def display(self):
        current = self.head
        if current is None:
            print("List is empty")  # Show message if list has no nodes
            return

        # Print each node's data followed by an arrow
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Indicate end of list


if __name__ == "__main__":
    # Create an instance of the linked list
    ll = SinglyLinkedList()

    print("\n=== Inserting Elements ===")
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_start(5)
    ll.insert_at_index(1, 15)  # List: 5 -> 15 -> 10 -> 20

    print("After insertions:")
    ll.display()

    print("\n=== Searching Elements ===")
    print("Index of 10:", ll.search(10))   # Expected: 2
    print("Index of 5:", ll.search(5))     # Expected: 0
    print("Index of 99:", ll.search(99))   # Expected: -1 (not found)

    print("\n=== Deleting Elements ===")
    ll.delete_at_index(1)  # Remove 15 → List: 5 -> 10 -> 20
    print("After deleting at index 1:")
    ll.display()

    ll.delete_at_index(0)  # Remove 5 → List: 10 -> 20
    print("After deleting head:")
    ll.display()

    ll.delete_at_index(5)  # Invalid index
    ll.delete_at_index(-1) # Invalid index

    print("\n=== Final List ===")
    ll.display()

    print("\n=== Testing Insertion at Out-of-Bounds Index ===")
    ll.insert_at_index(10, 50)  # Should print "Index out of bounds"

    print("\n=== Testing on Empty List ===")
    # Clear list manually
    ll = SinglyLinkedList()
    ll.display()                 # Should say "List is empty"
    ll.delete_at_index(0)       # Should print error
    print("Search in empty list:", ll.search(1))  # Should return -1
