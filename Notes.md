# NOTES
Author: ***THEFFTKID***

These notes were created woth the porpuse of get ready for my META interview, now I'm publishing it...

## The Parity
The parity of a binary word is **1** if the number of 1's in the word is od; otherwise, it's **0**. For example:

- The parity of 1000100 is 0.

## Arrays
It's the simplest data structure which is a continuos block of memory.

- Pull and push A[i] takes O(1) time.
- Deleting an element from an array entails moving all successive elements one over to the left to fill the vacated space.

Some useful:
- a in A for look into the array 
- ` 6 a in [9,8,10] == False`

### Copy and Deep Copy
Always consider the data should be collection.
- `B = A` Both lists are linked, if you modify one you will modify both. Because both are referring the same memory location.
- `B = A.copy()` B is going to be on a different memory location. But, if you have nested lists and use copy both objects are gping to be referring the same memory location.
- `B = copy.deepcopy(A)` make a new memory location and store the values of A.
- `B = list(A)` 

