from doubly_linked_list import DoublyLinkedList
# from doubly_linked_list import ListNode


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.storage = DoublyLinkedList()
        self.dictionary = {}
    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # Pull value out of the Dict using the key
        if key in self.dictionary:
            node = self.dictionary[key]
            self.storage.move_to_front(node)
            # return its value, it's a tuple
            # with a key and a value, so return the value from the node
            return node.value[1]
        else:  # if it equal's None then return None
            return None
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # if key already exists in cache, want to overwrite value.
        if key in self.dictionary:
            # update dict
            node = self.dictionary[key]
            # use tuple to return both key and it's value.
            # .value ties the value in the linked list
            # to the tuple we are storing in the dictionary
            node.value = (key, value)
            # now mark as most recently used, put in the head of the DLL
            self.storage.move_to_front(node)
            # if get to this point, nothing else matters, leave function
            return
        # If the cache is already at max capacity, oldest entry needs to be removed.
        if self.size == self.limit:
            # remove the oldest:
            # remove it from the DLL
            # remove it from the dict
            del self.dictionary[self.storage.tail.value[0]]
            self.storage.remove_from_tail()
            # changes the size of the list after deleting last entry
            self.size -= 1
        # Add a pair to the cache - add to dict and add it to nodes/DLL
        self.storage.add_to_head((key, value))
        self.dictionary[key] = self.storage.head
        self.size += 1  # add to the size of the list
