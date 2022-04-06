# NOTES
Author: ***THEFFTKID***

These notes were created with the porpuse of get ready for my META interview, now I'm publishing it...

## The Parity
The parity of a binary word is **1** if the number of 1's in the word is od; otherwise, it's **0**. For example:

- The parity of 1000100 is 0.

## Arrays
It's the simplest data structure which is a continuos block of memory.

- Pull and push A[i] takes O(1) time.
- Deleting an element from an array entails moving all successive elements one over to the left to fill the vacated space.
- It's faster write values from the back thanthe front.

Some useful:
- a in A for look into the array 
- ` 6 a in [9,8,10] == False`
- `A.reverse()` in-place
- `reversed(A)` iterator
- `A.sort()` in-place
- `sorted(A)` copy

### Copy and Deep Copy
Always consider the data should be collection.
- `B = A` Both lists are linked, if you modify one you will modify both. Because both are referring the same memory location.
- `B = A.copy()` B is going to be on a different memory location. But, if you have nested lists and use copy both objects are gping to be referring the same memory location.
- `B = copy.deepcopy(A)` make a new memory location and store the values of A.
- `B = list(A)` 

### bisect.py
Module for maintaining a list in sorted order without having to sort the list after each insertion, it uses th bisection method.
See the list_methods code for examples.

### Slicing
Similar to other languages python has a very easy way to slice list.
`[start:end] keep in min that **the end it's not** included in the selection. 

Ways:
- `[start:end]` from the start to one before end.
- `[:end]` from 0 to one before end.
- `[start:]` from start to end.
- `[start:end:step]` from the start to one before end each step.

### The Dutch National Flag Problem
The quicksort algorithm for sorting arrays proceeds recursively—it selects an element (the “pivot”), reorders the array to make all the elements less than or equal to the pivot appear first, followed by
all the elements greater t  han the pivot. The two subarrays are then sorted recursively. (META, 2022)

## Strings
The simplest way to understand these objects is an array-like structure...that are **inmutable**.

### Methods
- `s in t` evaluate if s is in t.
- `s.strip()` get rid of whitespaces.
- `s.starswtih(prefix)` Return `True` if string starts with the prefix, otherwise return `False`. Prefix can also be a tuple of prefixes to look for. **Case sensitive**.
- `s.endswith()` Return `True` if string ends with the prefix, otherwise return `False`. Prefix can also be a tuple of prefixes to look for. **Case sensitive**.
- `''.join('Soomething very important!')`
- `'Soomething very important!'.split('pattern')`
- `s.lower()` Return a copy of the string with all the cased characters converted to lowercase.
- `s.upper()` Return a copy of the string with all the cased characters converted to uppercase.
- `s.capitalize()` Return a copy of the string with its first character capitalized and the rest lowercased.

## Linked Lists
A singly linked list is a data structure that contains a sequence of nodes such that each node contains an object and a reference to the next node in the list. The first node is referred to as the head and the last node is referred to as the tail; the tail’s next field is null. The link list has no estrict linear ordering memory, the ordering of the elements is control by the data structure.

To see the `Class` implementation review the `linked_list.py` file.

## Stacks and Queues
Stacks support last-in, first-out semantics for inserts and deletes whereas queues are first-in, first-out.

Stack operations:
- Push: Add an element.
- Pop: Remove an element.

See `stacks_queues.py` file to see their implementations.

## Binary Trees
The *binary tree* helps to deal with hierarchies.
A binary tree is either empty, or a root node r together with a left binary tree and a right
binary tree. The subtrees themselves are binary trees. The left binary tree is sometimes referred to
as the left subtree of the root, and the right binary tree is referred to as the right subtree of the root.

### Definitions:
- Each node, except the root, is itself the root of a left subtree or a right subtree. 
- If l is the root of p’s left subtree, we will say l is the left child of p, and p is the parent of l.
- If a node is a left or a right child of p, we say it is a child of p. 
- **search path**: For any node there exists a unique sequence of nodes from the root to that node with each node in the sequence being a child of the previous node.
- The **depth** of a node n is the number of nodes on the search path from the root to n, not including
n itself.
- The **height** of a binary tree is the maximum depth of any node in that tree. 
- A **level** of a tree is all nodes at the same depth.