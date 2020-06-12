# PLANNING
# Use Array because it is the most space efficient, great run time complexity,
# only edits the last item and the length of Array is not changing.

# Just read the rubric and relized it is asking for either Stack or Queue and NOT Array.
# Will need to loop back after reverse.py to implement Stack LIFO- Last In First Out
from doubly_linked_list import DoublyLinkedList

# Ring buffer is a non-growable buffer with a fixed size.
# When the ring buffer is full and a new element is inserted,
# the oldest element in the ring buffer is overwritten with the newest element.
# ARRAY - ALL TESTS PASSING


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

# STACK- 2 TEST PASSING- RAN OUT OF TIME


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.current = None

# Appends/Adds the given element to the buffer
    def append(self, item):
        # is list at capacity?
        if self.capacity > self.storage.length:
            # no = add to tail
            self.storage.add_to_tail(item)
            # if there - replace with current value
            if self.storage.length == 1:
                self.current = self.storage.head
            else:
                # set current value to node
                self.current.value = item
            # if  not tail- move to next
            if self.current is not self.storage.tail:
                self.current = self.current.next
            else:
                self.current = self.storage.head

 # Get/Return all of the elements in the buffer in a list in their given order
    def get(self):
        # create empty list -loop through nodes
        content_list = []
        # while loop traversing through the list
        node = self.storage.head
        # adding value to the list once loop is done
        while node is not None:
            content_list.append(node.value)
            # move to next value
            node = node.next
        # return  list
        return content_list
