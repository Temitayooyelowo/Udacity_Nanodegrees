from queue import Queue
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = dict()
        self.LRU_tracker = Queue()
        self.curr_oper_capacity = 0
        self.max_oper_capacity = capacity

    def get(self, key):
        if key in self.cache:
            self.curr_oper_capacity +=1
            self.LRU_tracker.put(key)
            key = self.cache[key]
            self.remove_cache()
            return key
        # Retrieve item from provided key. Return -1 if nonexistent. 
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the least used item. 
        if key not in self.cache:
            self.remove_cache()
            self.curr_oper_capacity +=1
            self.cache[key] = value
            self.LRU_tracker.put(key)

    def remove_cache(self):
        if self.curr_oper_capacity == self.max_oper_capacity:
            removed_key = self.LRU_tracker.get()
            removed_key = self.cache.pop(removed_key, None)
            self.cache.pop(removed_key, None)
            self.curr_oper_capacity -= 1

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))     # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)



print(our_cache.get(3) )     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
