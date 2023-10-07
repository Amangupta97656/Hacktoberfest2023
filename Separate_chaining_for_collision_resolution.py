class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                # Update the value if the key already exists
                item[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        raise KeyError(f"Key '{key}' not found in the hash table")

    def remove(self, key):
        index = self.hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                self.table[index].remove(item)
                return
        raise KeyError(f"Key '{key}' not found in the hash table")

    def display(self):
        for index, items in enumerate(self.table):
            print(f"Index {index}: {items}")


if __name__ == "__main__":
    hash_table = HashTable(10)

    hash_table.insert("apple", 42)
    hash_table.insert("banana", 17)
    hash_table.insert("cherry", 98)

    print("Hash Table:")
    hash_table.display()

    print("Value for 'apple':", hash_table.get("apple"))
    print("Value for 'banana':", hash_table.get("banana"))

    hash_table.remove("banana")
    print("After removing 'banana':")
    hash_table.display()
