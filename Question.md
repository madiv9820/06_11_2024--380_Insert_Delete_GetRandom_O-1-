# [380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1?envType=study-plan-v2&envId=top-interview-150)

__Type:__ Medium <br>
__Topics:__ Array, Hash Table, Math, Design, Randomized <br>
__Companies:__ Bloomberg, Amazon, Google, Meta, TikTok, Uber, Affirm, Microsoft, Grammarly, Oracle, Yandex, LinkedIn, SoFi, Nvidia, Okta, X, Yelp, Pocket Gems, Apple, Adobe, DE Shaw, Goldman Sachs, Netflix, Sprinklr, Rubrik, Yahoo, Miro, Cisco
<hr>

Implement the `RandomizedSet` class:

- `RandomizedSet()` Initializes the `RandomizedSet` object.
- `bool insert(int val)` Inserts an item `val` into the set if not present. Returns `true` if the item was not present, `false` otherwise.
- `bool remove(int val)` Removes an item `val` from the set if present. Returns `true` if the item was present, `false` otherwise.
- `int getRandom()` Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the __same probability__ of being returned.

You must implement the functions of the class such that each function works in __average__ `O(1)` time complexity.
<hr>

### Examples

- __Example 1:__ <br>
__Input__ <br>
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"] <br>
[[], [1], [2], [2], [], [1], [2], []] <br>
__Output__ <br>
[null, true, false, true, 2, true, false, 2] <br> <br>
__Explanation__
RandomizedSet randomizedSet = new RandomizedSet(); <br>
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully. <br>
randomizedSet.remove(2); // Returns false as 2 does not exist in the set. <br>
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2]. <br>
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly. <br>
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2]. <br>
randomizedSet.insert(2); // 2 was already in the set, so return false. <br>
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
<hr>

### Constraints:

- <code>-2<sup>31</sup> <= val <= 2<sup>31</sup> - 1</code>
- At most <code>2 * 10<sup>5</sup></code> calls will be made to `insert`, `remove`, and `getRandom`.
- There will be __at least one__ element in the data structure when `getRandom` is called.