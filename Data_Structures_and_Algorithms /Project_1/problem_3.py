class Huffman:
    def __init__(self):
        self.root = None

def takeSecond(elem):
    return elem[1]

def get_frequency_of_characters(string):
    frequency_map = {}
    for char in string:
        if char in frequency_map:
            frequency_map[char] += 1
        else:
            frequency_map[char] = 1
    
    return sorted(frequency_map.items(),key=takeSecond)

a_great_sentence = "The bird is the word"
print(get_frequency_of_characters(a_great_sentence))
