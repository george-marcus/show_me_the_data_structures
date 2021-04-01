from collections import deque


class LRU_Cache(object):

    def __init__(self, capacity):
        if capacity is None or not isinstance(capacity, int):
            raise ValueError("Capacity should be a valid number")

        if capacity <= 0:
            raise ValueError("Capacity should be more than 0")

        self.capacity = capacity
        self.cache_dict = {}
        self.cache_usage_queue = deque()

    def append_to_left_of_usage_queue(self, key):
        # remove key from tail (if exists) and append it to head to indicate its recent use
        if self.cache_usage_queue and self.cache_usage_queue[-1] == key:
            self.cache_usage_queue.pop()

        self.cache_usage_queue.appendleft(key)

    def get(self, key):

        self.append_to_left_of_usage_queue(key)
        # defaults to -1 if nonexistant
        value = self.cache_dict.get(key, -1)
        print(value)
        return value

    def set(self, key, value):

        self.append_to_left_of_usage_queue(key)

        if len(self.cache_dict) == self.capacity:

            key_to_remove_from_cache = self.cache_usage_queue.pop()
            self.cache_dict.pop(key_to_remove_from_cache)

            print("key to remove:", key_to_remove_from_cache)

        self.cache_dict[key] = value
