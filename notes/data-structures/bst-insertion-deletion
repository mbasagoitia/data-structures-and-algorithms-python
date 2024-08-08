## Find

Starting at the root node, compare the element to find with the current node, then based upon if it is larger or smaller, search that node's left or right subtree. Repeat until you either find the element or nil. Return a pointer to either the node containing element or nil.

### Pseudo code for find

def find(node, search_key):
    if node is None:
        return node
    
    if node.key == search_key:
        return node
    elif node.key > search_key:
        return find(node.left, search_key)
    else:
    return find(node.right, search_key)

### Worst-case complexity

You may need to search the longest path of the tree (height h), so worst-case is O(h)
    - The height may be up to O(n) if unbalanced (# of nodes in tree) or O(log(n)) if balanced

## Insertion

We can slightly modify find to perform insert.

First, perform find (you wouldn't be inserting a node that already exists, so you will get a nil pointer returned). At that node, create the new node and add two child leaf nodes and a reference to the parent node.

### Pseudo code for insertion

def insert(node, key):

    if node is None:
        new_node = create_node(key)
        return new_node

    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    
    return node

## Deletion

Three cases when deleting a node (in case 2, this probably needs to be written as two separate cases, so really it's four separate cases)

1. The node to delete has two nil children (leaf node)
    - Simply replace that node with nil and it is effectively deleted
2. Only one child is nil
    - Replace the node with its child node by updating the child node's parent to the deleted node's parent
    - Determine whether the deleted node was a left or right child of the parent and update the parent node's left/right pointer accordingly
3. The node has two children that are not nil
    - Determine the successor of the node to be deleted (go one step to the right, then all the way to the left). Therefore, the successor is the smallest member of the node's right subtree.
    - Replace the node to be deleted with its successor and perform deletion on the successor as before (this node has one child, as determined by calculating successor...all the way to the left)


### Complexity

In the worst case, you will need to find the node and its successor, which together are O(h)

### Pseudo code for delete

def delete_node(root, key):
    if root is None:
        return root
    
    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        # Case 1: Node to be deleted is a leaf (no children)
        if root.left is None and root.right is None:
            return None
        
        # Case 2: Node to be deleted has one child
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        # Case 3: Node to be deleted has two children
        else:
            # Find the in-order successor (smallest node in the right subtree)
            successor = find_min(root.right)
            # Copy the successor's value to the node to be deleted
            root.key = successor.key
            # Delete the successor
            root.right = delete_node(root.right, successor.key)
    
    return root

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

## Tree Traversals

We need to traverse a tree if we are implementing a higher-level data structure such as a map/set/dictionary, we need to support iterators, map/filter operations, etc.

Visit every node in the tree in some order and do some operation at each node (could be print, send across network, etc.)

### Visitor Patterns

1. Inorder
    - For each node, visit the left child, the node itself, then the right child
2. Preorder
    - For each node, visit the node itself, the left child, then the right child
3. Postorder
    - For each node, visit the left child, the right child, then the node itself

These are recursive operations.

Example:

def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.key)
        in_order(node.right)

It's very easy to see where you place the print statement how you can modify this to support preorder or postorder patterns.

With inorder traversal, nodes are printed out in sorted order!

### Complexity

Traversing the tree takes O(n) time, where n is the number of internal nodes