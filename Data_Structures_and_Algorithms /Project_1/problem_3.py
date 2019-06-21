import heapq

class Node:
    def __init__(self, letter, frequency, left_child=None, right_child=None):
        self.letter = letter
        self.frequency = frequency
        self.left_child = left_child
        self.right_child = right_child

    def __lt__(self, other):
        return self.frequency < other.frequency

class Huffman:
    def __init__(self):
        self.root = None

    def encode(self, huffman_code, root_node, huffman_dict):
        if root_node is None:
            return huffman_dict

        if root_node.left_child is None and root_node.right_child is None:
            huffman_dict[root_node.letter] = huffman_code

        self.encode(f"{huffman_code}0", root_node.left_child, huffman_dict)
        self.encode(f"{huffman_code}1", root_node.right_child, huffman_dict)

    def decode(self, root_node, encoded_string, index):
        decoded_string = []
        while index < len(encoded_string) - 2:
            index = self.decode_helper(root_node, encoded_string, index, decoded_string)

        return decoded_string

    def decode_helper(self, root_node, encoded_string, index, decoded_string):
        if root_node is None:
            return index

        if root_node.left_child is None and root_node.right_child is None:
            decoded_string.append(root_node.letter)
            return index

        index += 1

        if encoded_string[index] == '1':
            index = self.decode_helper(root_node.right_child, encoded_string, index, decoded_string)
        else:
            index = self.decode_helper(root_node.left_child, encoded_string, index, decoded_string)

        return index


    def get_frequency_of_characters(self, new_string):
        frequency_map = {}
        for char in new_string:
            if char in frequency_map:
                frequency_map[char] += 1
            else:
                frequency_map[char] = 1

        return frequency_map

    def compress(self, frequency_dict):
        huffmanHeap = []

        # Iterating over values
        for letter, frequency in frequency_dict.items():
            heapq.heappush(huffmanHeap, Node(letter, frequency))

        while len(huffmanHeap) > 1:
            left_node = heapq.heappop(huffmanHeap)
            right_node = heapq.heappop(huffmanHeap)

            heapq.heappush(huffmanHeap, Node('Temp_Node', left_node.frequency + right_node.frequency, left_node, right_node))

        root_node = heapq.nlargest(1, huffmanHeap)
        return root_node[0]

    def run(self, sentence):
        frequency_map = self.get_frequency_of_characters(sentence)
        compressed = self.compress(frequency_map)

        huffman_code_map = {}
        self.encode("", compressed, huffman_code_map)

        huffman_string = ""
        i = 0
        while i < len(sentence):
            huffman_string += huffman_code_map[sentence[i]]
            i += 1

        # print(huffman_code_map)
        print(f"Encoded String: {huffman_string}")

        decoded_string = self.decode(compressed,huffman_string, -1)
        print(f"Decoded string is: {''.join(decoded_string)}")

a_great_sentence = "The bird is the word"
huffman = Huffman()
huffman.run(a_great_sentence)

# Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)
