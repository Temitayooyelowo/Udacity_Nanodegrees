Decided to use a queue for the LRU_tracker since it's FIFO and we needed to remove the least used element after a couple of sets and gets. I decided to use a dictionary for the cache since the set methods accepts a key and value.