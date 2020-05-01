class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.next = None

    def __repr__(self):
        str_result = f'({self.value}) '
        node = self.next
        while node:
            str_result += f'<- ({node.value})'
            node = node.next
        return str_result


class HashTable:
    def __init__(self, max_size):
        self.size = 0
        self.capacity = max_size
        self.buckets = [None] * self.capacity

    def __repr__(self):
        result_str = ''
        for idx, bucket in enumerate(self.buckets):
            result_str += f'{idx} {bucket} \n'
        return result_str

    def hash(self, string):
        str_len = len(string)
        hash_sum = 0
        for idx, char in enumerate(string):
            hash_sum += (idx + str_len) ** ord(char)
        return hash_sum % self.capacity

    def insert(self, key, value):
        self.size += 1
        hash = self.hash(key)
        node = self.buckets[hash]
        if not node:
            self.buckets[hash] = Node(key, value)
        else:
            while node.next:
                node = node.next
            node.next = Node(key, value)

    def search(self, key):
        hash = self.hash(key)
        node = self.buckets[hash]
        while node and key != node.key:
            node = node.next
        if not node:
            return None
        return node.value

    def remove(self, key):
        hash = self.hash(key)
        prev = None
        node = self.buckets[hash]

        while node and key != node.key:
            prev = node
            node = node.next
        if not node:
            return None
        self.size -= 1
        result = node.value
        if prev:
            prev.next = prev.next.next
        else:
            self.buckets[hash] = self.buckets[hash].next
        return result


if __name__ == '__main__':
    hash_table = HashTable(3)
    hash_table.insert('first', 99)
    hash_table.insert('firsd', 98)
    hash_table.search('firsd')
    hash_table.remove('first')
    print(hash_table)

