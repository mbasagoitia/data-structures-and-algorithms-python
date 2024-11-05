# B-Trees

Balanced tree data structure (not binary) achieving the same kind of balance as red-black trees. Optimized for large disk storage and databases.

Used for storing key-value pairs, supporting operations like:
- Find(key)
- Insert(key, value)
- Delete(key)

## Structure and Properties

Each node stores an array of m + 1 keys in sorted (ascending) order.

Each node contains m + 1 children/outgoing edges unless it is a leaf.

The length of every path from the root to the leaf is the same (completely balanced).

If you have m keys per node and depth d, then about m^d keys can be stored.

The depth of all leaves must be equal.

Each node of the tree other than the root has a number of keys m that is between d and 2d; d <= m <= 2d

For the root, number of nodes is between 0 and 2d keys; 0 <= m <= 2d

d is fixed ahead of time and is a property of the entire tree.

Only one key can be found anywhere in the tree; no repeated keys.

## Memory Hierarchy

In most modern computers, the CPU communicates with a series of caches, then the RAM, then the disk. B-Trees store data on the disk. There is a fixed cost of reading the sector of the disk on which the data exists, and you can read large amounts of data (individual nodes are big, so it's worthwhile to store them on the disk).

