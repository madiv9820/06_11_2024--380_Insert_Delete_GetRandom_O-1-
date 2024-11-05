import random

class RandomizedSet:
    def __init__(self):
        # Initialize a list to store elements for random access
        self.__list_item = []
        # Initialize a dictionary to map values to their existence in the set
        self.__map = {}

    def insert(self, val: int) -> bool:
        # Insert a value into the set
        # If the value already exists, return False
        if val in self.__map:
            return False
        # Mark the value as existing in the map
        self.__map[val] = True
        # Append the value to the list for random retrieval
        self.__list_item.append(val)
        return True

    def remove(self, val: int) -> bool:
        # Remove a value from the set
        # If the value does not exist, return False
        if val not in self.__map:
            return False
        # Remove the value from the map
        self.__map.pop(val)
        # Remove the value from the list
        self.__list_item.remove(val)
        return True

    def getRandom(self) -> int:
        # Return a random element from the list of items
        x = random.choice(self.__list_item)
        return x

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()