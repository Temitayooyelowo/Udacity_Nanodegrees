import unittest

from problem_5 import BlockChain, calc_hash

class Problem4(unittest.TestCase):

    def test_blockchain_with_1_element(self):
        first_data = 1
        expected_hash = calc_hash(first_data)

        first = BlockChain(first_data)

        curr_block = first.head_block
        self.assertEqual(curr_block.data, first_data)
        self.assertEqual(curr_block.previous_hash, 0)
        self.assertEqual(curr_block.hash, expected_hash)

    def test_blockchain_with_2_elements(self):
        first_data = 1
        second_data = 2

        expected_first_hash = calc_hash(first_data)
        expected_second_hash = calc_hash(second_data)

        root = BlockChain(first_data)
        root.append(second_data)

        root_block = root.head_block

        curr = root_block

        while curr.next:
            curr = curr.next

        self.assertEqual(curr.data, second_data)
        self.assertEqual(curr.previous_hash, expected_first_hash)
        self.assertEqual(curr.hash, expected_second_hash)
    
    def test_empty_blockchain(self):
        root = BlockChain()

        self.assertEqual(root.head_block, None)

    def test_append_after_empty_blockchain(self):
        first_element = 10000
        expected_hash = calc_hash(first_element)

        root = BlockChain()
        root.append(first_element)

        curr_block = root.head_block
        self.assertEqual(curr_block.data, first_element)
        self.assertEqual(curr_block.previous_hash, 0)
        self.assertEqual(curr_block.hash, expected_hash)

if __name__ == '__main__':
    unittest.main()