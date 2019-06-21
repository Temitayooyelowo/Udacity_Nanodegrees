import unittest

from problem_3 import Huffman
class Problem2(unittest.TestCase):

    def test_get_frequency_of_characters(self):
        test_sentence = "test send"
        huffman = Huffman()
        result = huffman.get_frequency_of_characters(test_sentence)

        self.assertEqual(result['t'],2)
        self.assertEqual(result['e'], 2)
        self.assertEqual(result['s'], 2)
        self.assertEqual(result[' '], 1)
        self.assertEqual(result['n'], 1)
        self.assertEqual(result['d'], 1)

    def test_encode(self):
        test_sentence = "test"
        huffman = Huffman()
        result = huffman.huffman_encoding(test_sentence)

        self.assertEqual(result['huffman_string'], "010110")

    def test_decode_without_end_space(self):
        test_sentence = "Testing the huffman tree"
        huffman = Huffman()
        huffman_encoded = huffman.huffman_encoding(test_sentence)

        result = huffman.huffman_decoding(huffman_encoded['root_node'], huffman_encoded['huffman_string']);

        self.assertEqual(result, test_sentence)

    def test_decode_with_end_space(self):
        test_sentence = " Testing the huffman tree "
        huffman = Huffman()
        huffman_encoded = huffman.huffman_encoding(test_sentence)

        result = huffman.huffman_decoding(huffman_encoded['root_node'], huffman_encoded['huffman_string']);

        self.assertEqual(result, test_sentence)

if __name__ == '__main__':
    unittest.main()
