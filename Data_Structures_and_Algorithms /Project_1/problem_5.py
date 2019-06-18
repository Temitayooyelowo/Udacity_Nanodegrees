import hashlib

from time import asctime

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(data)
      self.next = None

    def calc_hash(self, data):
      sha = hashlib.sha256()
      hash_str = str(data).encode('utf-8')
      sha.update(hash_str)

      return sha.hexdigest()

    def __str__(self):
        s = "______________________________\n"
        s += f"Timestamp: {self.timestamp}\n"
        s += f"Data: {self.data}\n"
        s += f"Previous Hash: {self.previous_hash}\n"
        s += f"SHA256 Hash: {self.hash}\n"
        s += "______________________________\n"

        return s

class BlockChain:
    def __init__(self, new_data):
        self.head_block = Block(self.generate_timestamp(), new_data, 0)

    def generate_timestamp(self):
            return asctime()

    def append(self, new_data):
        curr = self.head_block

        while curr.next is not None:
            curr = curr.next
        curr.next = Block(self.generate_timestamp(), new_data, curr.hash)
        # print(curr)
        # print(curr.next)
        # print(curr.next.next)

    def __str__(self):
        curr = self.head_block

        # s = "Blockchain\n"
        # while curr:
        #     s += "\n"
        #     s += curr

        # return s

first = BlockChain(1)
first.append(2)
first.append(3)
first.append(4)
first.append(10)

curr = first.head_block
while curr:
    print(curr)
    curr = curr.next