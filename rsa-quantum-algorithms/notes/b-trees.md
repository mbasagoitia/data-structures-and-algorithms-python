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

# Methods

Find(k): check if a key exists in the tree; returns True or False; not the associated value

Steps:

- Search root for key
- If not in root, find smallest ki that is > k and traverse the pointer to the left child of that ki; if such a ki doesn't exist, k is larger than all values in that node, so traverse the right subtree of km (last value in node)
- Traverse this new node searching for k
- Repeat until you find k or reach a leaf node

Insert:

- Start with the find operation, which will fail because you cannot have duplicate keys in a B-Tree, and you will end up in a leaf node. 
- If the number of keys in the current leaf node is not at maximum (2d), simply insert the key at the appropriate place, shifting keys as necessary.
- If there is no space at the current leaf node (already has 2d keys), we have several strategies:
    - Median split: Our target node has 2d + 1 keys; split it into 2 nodes of d keys each and a median; try to promote/insert the median key one step higher (parent node). If the parent node has no space, continue the process one level up. This how the data structure grows in height.

Delete:

- Locate the key with the find operation.
- Locate the key's successor, which is found by going one step right (right child node), then traversing all the way to the left until you reach a leaf node (finding the smallest key of the left child node at each step).
- Delete the successor from its current place and place it where the original node to delete was.
- In this way, the key that we are deleting is always in a leaf.
- What if deleting a key at a leaf node violates the property d <= m <= 2d? Two cases:
    - Check the sibling node(s). If the sibling has > d keys, we can **"borrow"** a key from that sibling.
    - If we are borrowing from the right sibling, after deletion from the current node, we take the leftmost key, move it up to the parent, and take the key from the parent that it is replacing and move it down to the original node. If it is left sibling, same thing but with rightmost key.
    - If no available siblings have keys to spare without violating this property, we will **merge** our current node with a sibling node AND the parent node of those two siblings to create a single node. Pointer updates and recursive deletion will be necessary.