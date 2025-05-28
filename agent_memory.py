
class Memory:
    def __init__(self):
        self.memory = []

    def add(self, item):
        """Add an item to the memory."""
        self.memory.append(item)

    def get(self, index):
        """Retrieve an item from the memory by index."""
        if 0 <= index < len(self.memory):
            return self.memory[index]
        else:
            raise IndexError("Index out of range")

    def clear(self):
        """Clear the memory."""
        self.memory.clear()

    def get_memory(self):
        """Return the entire memory."""
        return self.memory

    def __len__(self):
        """Return the number of items in memory."""
        return len(self.memory)
    
    def __str__(self):
        """Return a string representation of the memory."""
        return f"Memory({self.memory})"