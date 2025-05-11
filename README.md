# Linked-Lists

**Name:** Maina Tiffany Wanjiru  
**Admission Number:** 189592  

## Description
This repository shows class-based implementation of a Singly Linked List in Python.

## Components
- Insert a node at the **start** of the list
- Insert a node at the **end** of the list
- Insert a node at a **specific index**
- Delete a node at a **specific index**
- **Search** for a value and return its index
- **Display** all node values in the list

## Class Structure

### `Node`
Represents each element of the linked list.

- `data`: Holds the value.
- `next`: Points to the next node (or `None` if it's the last).

### `SinglyLinkedList`
Manages the linked list operations.

#### Methods:

- `insert_at_start(data)` – Insert a new node at the beginning.
- `insert_at_end(data)` – Insert a new node at the end.
- `insert_at_index(index, data)` – Insert at a specific index.
- `delete_at_index(index)` – Delete the node at a specific index.
- `search(value)` – Return the index of the first occurrence of the value.
- `display()` – Print the values of the list.