# Test environment

# Parity block-code:
# def parity(x):
#     result = 0
#     while x:
#         result ^= x & 1
#         x >>= 1
#     return result

# parity(10)

# Integer sorted array block-code:
# def even_odd(A):
#     next_even, next_odd = 0, len(A) - 1
#     while next_even < next_odd:
#         if A[next_even] % 2 == 0:
#             next_even += 1
#         else:
#             A[next_even], A[next_odd] = A[next_odd], A[next_even]
#             next_odd -= 1

# even_odd([1,5,6,7,2,4])

# The Dutch National Flag 
import random


RED, WHITE, BLUE = range(3)

def Dutch_flag(pivot_index, A):
    pivot = A[pivot_index]
    # First pass: group elements smaller thanm a pivot
    for i in range(len(A)):
        # Look for a smnaller element
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break
    # Second pass: group elements larger than a pivot.
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        # Look for a larger element. Stop when we reach an element less than
        # pivot, since first pass has moved them to the start of A
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break

A = [random.randint(1,5) for a in range(5)]
Dutch_flag(3,A)