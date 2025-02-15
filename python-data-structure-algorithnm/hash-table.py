# Hash Function
def simple_hash(key):
    return hash(key) % 10


# Creating a hash table using a dictionary
hash_table = {"name": "Alice", "age": 30, "city": "New York"}

# Accessing elements
print(hash_table["name"])  # Output: Alice

# Adding elements
hash_table["job"] = "Engineer"

# Removing elements
del hash_table["age"]

# Iterating through the hash table
for key, value in hash_table.items():
    print(f"{key}: {value}")


# Implementing a Hash Table from Scratch
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Initialize buckets as lists (chaining)

    def _hash_function(self, key):
        return hash(key) % self.size  # Simple hash function

    def insert(self, key, value):
        index = self._hash_function(key)
        for pair in self.table[index]:  # Check if the key already exists
            if pair[0] == key:
                pair[1] = value  # Update value if key exists
                return
        self.table[index].append([key, value])  # Insert new key-value pair

    def search(self, key):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]  # Return value if key is found
        return None  # Key not found

    def delete(self, key):
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)  # Remove the pair
                return True
        return False  # Key not found

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")


# Example Usage
hash_table = HashTable()

# Insert key-value pairs
hash_table.insert("name", "Alice")
hash_table.insert("age", 30)
hash_table.insert("city", "New York")

# Search for a key
print("Search 'name':", hash_table.search("name"))

# Delete a key
hash_table.delete("age")

# Display the hash table
hash_table.display()
