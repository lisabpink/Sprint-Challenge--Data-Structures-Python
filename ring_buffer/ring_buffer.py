# PLANNING
# Use Array because it is the most space efficient, great run time complexity,
# only edits the last item and the length of Array is not changing.

# Ring buffer is a non-growable buffer with a fixed size.
# When the ring buffer is full and a new element is inserted,
# the oldest element in the ring buffer is overwritten with the newest element.
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None]*capacity
        self.current = 0

# Appends/Adds the given element to the buffer
    def append(self, item):
        self.storage[self.current] = item
        self.current += 1
        if self.current == self.capacity:
            self.current = 0

 # Get/Return all of the elements in the buffer in a list in their given order
    def get(self):
        return [x for x in self.storage if x is not None]
