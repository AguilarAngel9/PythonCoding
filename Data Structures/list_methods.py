# List methods
from audioop import reverse
import bisect

A = [1,3,4,5]

bisect.insort_left(A,8)
# First runs bisect_left() an then runs the insert().

bisect.insort_right(A,8)
# First runs bisect_left() an then runs the insert().

print(bisect.bisect_left(A,8))
# Return the i position where the int should be inserted, if the number already exists it return the position before it.

print(bisect.bisect_right(A,8))
# Return the i position where the int should be inserted, if the number already exists it return the position after it.

A.reverse() # Reverse the array in-place

list(reversed(A)) # Returns an iterator with the array reversed.

def is_palindromic (s):
    # Note that s[~i] for i in [0, len(s) - 1] is s[-(i + 1)].
    # all() evaluates if all the array is true
    # s[i] == s[~i] compare each position with it's complement using the complement operator.
    return all(s[i] == s[~i] for i in range(len(s) // 2))

print(is_palindromic('abba'))