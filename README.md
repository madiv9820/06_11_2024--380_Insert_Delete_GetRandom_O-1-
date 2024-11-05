# Insert Delete GetRandom O(1)

- ### Intuition
    The problem is to design a data structure that supports three operations:
    1. **Insert**: Add a value to a collection if it is not already present.
    2. **Remove**: Remove a value from the collection if it exists.
    3. **GetRandom**: Retrieve a random element from the collection with constant time complexity.

    We want to achieve this with efficient time complexities for each of these operations.

- ### Approach
    We can leverage three data structures to efficiently handle the operations:
    1. **Set (`__random_Set`)**: This ensures that we only have unique elements in the collection and allows for constant-time membership checks (`O(1)`).
    2. **List (`__list_item`)**: This allows us to efficiently retrieve a random element, as list indexing is `O(1)` and we can store the elements in the order they were inserted.
    3. **Dictionary (`__map`)**: This is used for quick lookups to check if an element exists, which allows for constant-time insertion and deletion (`O(1)`).

    - #### Insertion (`insert`):
        - When inserting a value, we check if the value already exists in the dictionary (`__map`). If it does, we return `False` (indicating failure to insert).
        - If the value is not in the dictionary, we add it to both the set and the list. We also mark it as existing in the dictionary.

    - #### Removal (`remove`):
        - When removing a value, we first check if the value exists in the dictionary.
        - If it does, we remove it from the set, dictionary, and list. This ensures that the value is fully removed from the data structure.

    - #### Random Element Retrieval (`getRandom`):
        - The `getRandom` method simply returns a random element from the list using `random.choice()`. This operation is `O(1)` because list indexing and access is constant time.

- ### Example Walkthrough

    Let’s consider an example with the following operations:

    1. **Insert 1**:
        - Insert the value `1`. The dictionary becomes `{1: True}`, the set becomes `{1}`, and the list becomes `[1]`. Return `True` (success).

    2. **Insert 2**:
        - Insert the value `2`. The dictionary becomes `{1: True, 2: True}`, the set becomes `{1, 2}`, and the list becomes `[1, 2]`. Return `True` (success).

    3. **Remove 1**:
        - Remove the value `1`. The dictionary becomes `{2: True}`, the set becomes `{2}`, and the list becomes `[2]`. Return `True` (success).

    4. **GetRandom**:
        - Call `getRandom`. Since the only remaining value is `2`, it returns `2`. This operation is `O(1)`.

    5. **Insert 3**:
        - Insert the value `3`. The dictionary becomes `{2: True, 3: True}`, the set becomes `{2, 3}`, and the list becomes `[2, 3]`. Return `True` (success).

    6. **GetRandom**:
        - Call `getRandom`. The method could return either `2` or `3` randomly. Each element has an equal chance of being chosen.

- ### Time Complexity
    - **Insert Operation**: `O(1)`
        - Checking if an element exists in the dictionary (`__map`) takes `O(1)`.
        - Adding the element to the set and list also takes `O(1)` time.
  
    - **Remove Operation**: `O(1)`
        - Checking if the element exists, removing it from the dictionary, set, and list all take `O(1)` time.
    
    - **GetRandom Operation**: `O(1)`
        - Retrieving a random element from the list takes constant time (`O(1)`).

    Overall, each operation (`insert`, `remove`, and `getRandom`) runs in constant time `O(1)`.

- ### Space Complexity
    - The space complexity is determined by the storage used for the set (`__random_Set`), list (`__list_item`), and dictionary (`__map`).
        - **Set**: Requires space for storing unique elements.
        - **List**: Requires space for storing the elements in the order they were inserted.
        - **Dictionary**: Requires space for mapping each element to its existence.
    
    Therefore, the space complexity is **O(n)**, where `n` is the number of elements stored in the data structure.

- ### Code
    ```python3 []
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
    ```