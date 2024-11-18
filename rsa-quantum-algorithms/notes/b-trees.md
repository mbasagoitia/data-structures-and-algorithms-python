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

## Methods

Find(k): check if a key exists in the tree; returns True or False; not necessarily the associated value

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
    - Lending scheme: Ensures that splitting only happens when the node and its siblings are at capacity. If the node has a right sibling and the right sibline has < 2d keys, shift the rightmost key of the current node up to the parent and move the rightmost key of the parent down to the right sibling (as the leftmost node). Mirror the process for the left sibling node. If both left and right siblings are "full," then perform the median split strategy.

Delete:

- Locate the key with the find operation.
- Locate the key's successor, which is found by going one step right (right child node), then traversing all the way to the left until you reach a leaf node (finding the smallest key of the left child node at each step).
- Delete the successor from its current place and place it where the original node to delete was.
- In this way, the key that we are deleting is always in a leaf.
- What if deleting a key at a leaf node violates the property d <= m <= 2d? Two cases:
    - Check the sibling node(s). If the sibling has > d keys, we can **"borrow"** a key from that sibling.
    - If we are borrowing from the right sibling, after deletion from the current node, we take the sibling's leftmost key, move it up to the parent, and take the key from the parent that it is replacing and move it down to the original node. If it is left sibling, same thing but with rightmost key.
    - If no available siblings have keys to spare without violating this property, we will **merge** our current node with a sibling node AND the parent node of those two siblings to create a single node. Pointer updates and recursive deletion will be necessary.

    def handle_full_node(self, debug=True):
        """Try to lend a key to left or right sibling if they have < 2*self.d keys.
           Otherwise, split the node into two.
        
        Return value:
        
            If we can successfully lend the key/pointer to either sibling, return None
            Otherwise, return whatever result self.split_node_into_two() does.
        """
        # use debug key to print useful messages for your debugging
        assert len(self.keys) == 2 * self.d + 1
        d = self.d
        if self.parent == None : # already at the root
            return self.split_node_into_two() # no other option but to split
        # unpack the parent pointer
        (parent_node, parent_idx) = self.parent
        # self is the child of parent_node and equals parent_node.pointers[parent_idx]
        ## TODO:
        ##   1. Check if I have a right sibling node, fetch right sibling node and find out if it has space.

        left_sibling = parent_node.pointers[parent_idx - 1] if parent_idx > 0 else None
        right_sibling = parent_node.pointers[parent_idx + 1] if parent_idx < len(parent_node.pointers) - 1 else None

        if right_sibling is not None and len(right_sibling.keys) < 2 * d:
            right_sibling.keys.insert(0, parent_node.keys[parent_idx])
            parent_node.keys[parent_idx] = self.keys.pop()

            if self.pointers:
                right_sibling.pointers.insert(0, self.pointers.pop())

            self.fix_parent_pointers_for_children()
            return None

        elif left_sibling is not None and len(left_sibling.keys) < 2 * d:
            left_sibling.keys.append(parent_node.keys[parent_idx - 1])
            parent_node.keys[parent_idx - 1] = self.keys.pop(0)

            if self.pointers:
                left_sibling.pointers.append(self.pointers.pop(0))

            self.fix_parent_pointers_for_children()
            return None

        else:
            return self.split_node_into_two()
            ##        1.1. If right sibling exists and has space, lend my rightmost key and pointer to the right sibling as its leftmost key and pointer
            ##        1.2 Do not forget to call the function fix_parent_pointers since parent pointers will get invalidated.
            ##        1.2 Insertion is done, return None
            ##   2. Check if I have a left sibling node, fetch left sibling node and find out if it has space
            ##        2.1 If left sibling exists and has space, lend my leftmost key and pointer to left sibling as its rightmost key and pointer 
            ##        3.3 Insertion is done, return None

        raise NotImplementedError


        # Implementation of Ukkonen's algorithm
def construct_suffix_trie(orig_str, debug=False):
    root = SuffixTrieNode(0, orig_str) # create a root node with id = 0
    root.add_suffix_link(root) # make the root suffix link to itself
    node_list= [root] # maintain a list of all nodes for our bookkeeping
    addr = TrieAddress(root, None, 0) # initialize the address to point to the root
    n = len(orig_str)
    for i in range(n): # go through each position in the original string
        # We will now work on phase number i of the algorithm
        c = orig_str[i] 
        if debug:
            print(f"Phase # {i}: inserting {c}")
        node = None # initialize pointers to node and new_node to None
        new_node = None # these pointers will help us with the adding of suffix links for newly created nodes later
        dest = addr.traverse_next(c) # try to move from the current address to a new address given the character `c`.
        if dest != None:
            addr = dest # dest exists, we simply update addr to that destination and continue
        else: # no such destination exists. Rule # 2 applies and we have to create new internal nodes
            while dest == None and not addr.is_at_root(): # while the current addr does not have a destination for next character c, and it is not at the root
                if debug:
                    print(f"Creating new node with char {orig_str[i]} at {addr}")
                # create a new node and a new leaf at the current address
                (new_node, new_leaf, newly_created) = addr.create_new_edge_at(orig_str, i, len(node_list))
                if debug:
                    print(f"Created new node: {new_node.id}")
                
                if node != None and not node.is_root():
                    node.add_suffix_link(new_node) # add a suffix link from the previously created node to the new node
                    if debug:
                        print(f"D1: Adding Suffix Link:{node.id} ---> {new_node.id}")
                if newly_created:
                    node_list.append(new_node) # if it is freshly created then add it to the list of nodes
                node_list.append(new_leaf)
                node = new_node # update pointer to previously created node
                addr = addr.compute_suffix() # compute the suffix of the address
                assert addr != None, f"Suffix computation failed. "
                dest = addr.traverse_next(c) # see if there is a destination with char c from the newly computed address
                #if dest != None: # if there is a destination
                #    new_node.add_suffix_link(addr.node) # add the last suffix link
                #    if debug:
                #        print(f"D2: Adding Suffix Link: {new_node.id} --> {addr.node.id}")
            # We are out of the loop
            # add a suffix link from the last created node to the current address.
            if node != None:
                if debug:
                    print(f"D3: Adding Suffix Link: {new_node.id} --> {addr.node.id}")
                node.add_suffix_link(addr.node)
            
            if dest == None:
                # if this happens, we are at the root
                # insert the char `c` here.
                assert addr.is_at_root()
                (new_node, new_leaf, newly_created) = addr.create_new_edge_at(orig_str, i, len(node_list))
                assert not newly_created 
                node_list.append(new_leaf)
            else:
                # this indicates that the char c already exists.
                addr = dest
        
        if debug:
            print("currently at: ", addr)
            draw_networkx_graph(root, end=i+1, highlight_addr=addr, filename=f"{orig_str}.{i}.png")
    return root





def find_longest_palindrome(s):
    # Step 1: Reverse the string
    reversed_s = s[::-1]
    
    # Step 2: Construct suffix trees for both the original string and the reversed string
    root_s = construct_suffix_trie(s)
    root_reversed_s = construct_suffix_trie(reversed_s)
    
    # Step 3: Initialize variables for tracking the longest palindrome
    longest_palindrome = ""
    n = len(s)
    
    # Step 4: Perform a depth-first traversal to compare nodes from both suffix trees
    stack = [(root_s, root_reversed_s, 0)]  # Stack to keep track of nodes from both trees and the current match length
    
    while stack:
        node1, node2, length = stack.pop()
        
        if node1 is None or node2 is None:
            continue
        
        # Check all pairs of children of the current nodes in both trees
        for child1 in node1.children:
            for child2 in node2.children:
                if child1.char == child2.char:  # The characters match
                    # Build the substring formed by the matching prefix
                    lcp_substring = s[child1.start: child1.start + length + 1]
                    
                    # Check if this substring is a palindrome
                    if lcp_substring == lcp_substring[::-1] and len(lcp_substring) > len(longest_palindrome):
                        longest_palindrome = lcp_substring
                    
                    # Add children to stack for further comparison
                    stack.append((child1, child2, length + 1))
    
    return longest_palindrome



    # your code here
    print("original string", orig_str)

    # Case 1: Parent is the root (p is the root)

# Suppose the node 𝑛's parent 𝑝 is the root node of the trie (𝑝=𝑟), and the edge 𝑟→𝑛 corresponds to the substring: 𝑠[𝑙𝑜],…,𝑠[ℎ𝑖].

# The substring that would correspond to the unique path from the root to the suffix node of 𝑛 is

# s[lo + 1] ... s[hi]
    print("current low and high:", lo, hi)
    print("parent's suffix link is node:", p.suffix_link.id)
    
    print("current node:", n.id, orig_str[lo::hi + 1])
    if lo + 1 == hi:
        print("my suffix should be the dest from the node's list of edges whose string is:", orig_str[hi])
    else:
        print("my suffix should be the dest from the node's list of edges whose string is:", orig_str[lo + 1:hi + 1])
    print("outgoing edges of root:", len(root.outgoing_edges.items()))
    print("Edges of root node:")
    for (_, og_edge) in root.outgoing_edges.items():
        print("ID:", og_edge.dest.id)
        print("edge lo and hi", og_edge.lo, og_edge.hi)
        if og_edge.lo == og_edge.hi:
            print("represents:", orig_str[og_edge.lo])
        else:
            print("represents:", orig_str[og_edge.lo:og_edge.hi + 1])