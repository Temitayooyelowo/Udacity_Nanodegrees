import unittest

from problem_1 import LRU_Cache
class Problem1(unittest.TestCase):

    def test_empty_cache(self):
        our_cache = LRU_Cache(5)

        result = our_cache.get(1)
        self.assertEqual(result, -1)
    
    def test_cache_before_limit(self):
        our_cache = LRU_Cache(3)

        our_cache.set(1, 1)
        our_cache.set(2, 2)
        our_cache.set(3, 3)

        self.assertEqual(our_cache.curr_oper_capacity, 3)
        self.assertEqual(our_cache.get(1), 1)
    
    def test_past_max_capacity(self):
        our_cache = LRU_Cache(5)
        our_cache.set(1, 1)
        our_cache.set(2, 2)
        our_cache.set(3, 3)
        our_cache.set(4, 4)


        our_cache.get(1)
        self.assertEqual(our_cache.get(2), 2)
        self.assertEqual(our_cache.get(1), -1)
    
    def test_invalid_element(self):
        our_cache = LRU_Cache(2)
        our_cache.set(1, 1)

        self.assertEqual(our_cache.get(9), -1)


if __name__ == '__main__':
    unittest.main()