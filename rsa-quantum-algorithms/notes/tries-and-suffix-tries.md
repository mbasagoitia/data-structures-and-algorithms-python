# Tries

Compact, tree-like data structures that work over string data, used to store a set of strings T1 ... Tn

Every path from the root to a leaf is a unique word in the trie.

Ex. 'abacus$' where the dollar character is the string terminator character, and also is given an index in the string. Strings are zero-indexed.

Characters are drawn from some alphabet, AKA sigma, such as {a, b, c, ...}, {A, C, T, G}, {0, 1}, ASCII, etc.

Lexicographic/dictionary ordering considers character codes and their numerical values to compare strings.

Sorting strings in this order no longer makes trivial comparisons; in the worst case, the time is proportional to the length of the shortest string, so sorting T1 ... Tn strings takes O(n log n * M) time where M is the length of the longest string. This is using sorting techniques like merge sort and insertion sort.

## Uses

- Pattern-matching
- String sorting
- Text search/find and replace
- Autocomplete
- Genome databases

## Structure

Tree with a root node and outgoing edges between nodes. Each edge is labeled by a character, and we include the terminator ($) character which connects us to a leaf node. The number of leaf nodes should correspond to the number of strings in the set.

For any node in the trie, there exists at most **one** outgoing edge for a unique character c.

The $ character helps us know when a word has ended; this is very important if a word is a subset of a larger word--it will have a leaf node with $ connecting it to signify that itself is the end of a word.

## Node Structure

Root/internal nodes have the same structure: node n contains outgoing edges to different nodes, n1, n2, n3, etc. Node n can be represented as an array of all characters in sigma with pointers to n1, n2, n3 and null pointers to all other characters.

However, arrays aren't very efficient, especially for large alphabets. Hashtables may be used, though they don't support (efficient) iteration.

## Searching

Given a set of strings {T1 ... Tn}, find all string indices that start with some pattern p.

We start from the root node and follow all matching edges. We then look for all possible nodes from the last node of the pattern you're searching for. Furthermore, we know that no strings match the pattern if there is no outgoing edge to any character in the middle of the pattern. This method gives us time complexity p (length of pattern) + size of result instead of n(number of strings) * p.

## Sorting

Given a set of strings {T1 ... Tn}, print out all the strings in sorted order. 

Simply perform an inorder traversal of the trie.

We can also find lexicographically nearest string by following the tree until it diverges from the target string, then following the leftmost path to a leaf.

We can find all possible ways to complete a given string by following all leaf nodes from the last node of the sequence (autocomplete).

# Suffix Tries

Also known as suffix trees.

A trie built out of all suffixes of a given string s. In python, s[i:n] for all i up to the length of the string.

Ex. "abracadabra$" suffixes -> "bracadabra$", "racadabra$", "acadabra$" ... "a$", "$"

The string is also a suffix of itself.

We would denote in each leaf node which index the given suffix starts from in the original string.

In this kind of data structure, we can see if a pattern appears anywhere in the string. We can furthermore determine which index it starts at by following the current path down to the leaf and reading its data.

We can also count how many times a pattern appears by following the current path down and counting the number of leaves below that node. We can augment the suffix trie with extra information such as storing how many leaf nodes are below a particular node.

## Compressed Representation

When we have many internal nodes with only one child, we can save space by instead of assigning each edge only one character, compressing it into a string of all characters in that path. We can represent the strings on each edge as their starting and ending indices rather than the actual string itself, such as [1, 4] or [4, 4] if it is the same character.

The number of internal nodes in a compressed suffix trie is <= the number of leaves. Nodes with only one child are compressed away.

The number of leaves is equal to the length of the string.

Therefore, the number of nodes in a compressed suffix trie is <= 2 * the length of the string.

## Suffix Links

Link internal nodes to other internal nodes.

For a node representing c + alpha (the rest of the string), the suffix link points to the node at which we can find alpha.

We can use algorithms with suffix links to find the longest common subsequence, longest palindrome, etc. between strings.

## Constructing Suffix Tries (Inefficient)

Start with building a compressed version of the tree (have string representations of each suffix instead of individual characters), then when you need to add a new suffix to an already existing character or substring, create a new node at that point and split the sequence.

Suffix links can be added after the fact.