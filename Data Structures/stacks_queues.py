
import collections

class Stack:
    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax', 
    ('element','max'))

    def __init__(self):
        self._element_with_cached_max = []
    
    def empty(self):
        return len(self._element_with_cached_max) == 0
    
    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._element_with_cached_max[-1].max
    
    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self._element_with_cached_max.pop().element
    
    def push(self, x):
        self._element_with_cached_max.append(
            self.ElementWithCachedMax(x, x if self.empty() else max(x, self.max()))
        )

S = Stack()


class Queue:

    def __init__(self):
        self._data = []
    
    def enqueue(self, x):
        self._data.append(x)
    
    def dequeue(self):
        return self._data.pop(0)
    
    def max(self):
        return max(self.data)

