class Huffman:
    def __init__(self):
        self.root = None

def get_frequency_of_characters(string):
    frequency_map = {}
    for char in string:
        if char in frequency_map:
            frequency_map[char] += 1
        else:
            frequency_map[char] = 1
    
    return frequency_map.values()

a_great_sentence = "The bird is the word"
print(get_frequency_of_characters(a_great_sentence))
