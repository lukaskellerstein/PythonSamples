# ONLY RIGHT CUSTOM IMPLEMENTATION

class HashTable:
    def __init__(self):
        self.table = [None] * 127
        self.size = 0

    def _hash(self, key):
        hash_value = sum(ord(char) for char in key)
        return hash_value % len(self.table)

    def set(self, key, value):
        index = self._hash(key)
        self.table[index] = (key, value)
        self.size += 1

    def get(self, key):
        index = self._hash(key)
        if self.table[index] and self.table[index][0] == key:
            return self.table[index]
        return None

    def remove(self, key):
        index = self._hash(key)
        if self.table[index] and self.table[index][0] == key:
            self.table[index] = None
            self.size -= 1
            return True
        return False


# Example usage
ht = HashTable()

# Add
ht.set("Canada", 300)
ht.set("France", 100)
ht.set("Spain", 110)

# Get
print(ht.get("Canada"))  # Output: ('Canada', 300)
print(ht.get("France"))  # Output: ('France', 100)
print(ht.get("Spain"))   # Output: ('Spain', 110)

# Remove
print(ht.remove("Spain"))  # Output: True
print(ht.get("Spain"))     # Output: None
