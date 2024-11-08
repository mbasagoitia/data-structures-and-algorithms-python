# Ukkonen's Algorithm

Algorithm for constructing suffix tries in linear time.

Constructs a series of tries T1 ... Tm where m is the length of the string.

At each step, Ti is a suffix trie for the string up to length i.

T0 represents the empty string, which is the root.

During construction, the end of suffixes are implicit, but the entire trie becomes explicit by the end (clear endings $ to each suffix).

m phases to the algorithm and each phase builds up from Ti -> Ti + 1

## High-Level Overview (Inefficient Version)

Ex. banana

1st phase: suffix trie for b = b
2nd phase: suffix trie for ba = ba, a
3rd phase: suffix trie for ban = ban, an, n
4th phase: suffix trie for bana = bana, ana, na, a
etc.

After m phases, we need to add the termination character $

Since the current version of the trie is implicit (some unique paths/suffixes end in the middle of another suffix), we need to traverse through all possible suffixes of the original string and add these characters at the end of each one:

- banana$
- anana$
- nana$
- ana$
- na$
- a$

However, this will require splitting into new paths/nodes at some places to make the trie explicit.

Add suffix links along the way.

This method uses two loops, outer from T0 to Tm and inner from 0 to i where i is the current "version" of the trie Ti.

Insertion into Ti must follow these rules:

alpha = the current string you are trying to insert 

1.  If the path for alpha leads to a leaf node, extend that edge by 1 character
- If the path for alpha does not lead to a leaf node,
    2. If the last character is not included in the current path and the next node after that is not a leaf, create a new internal node and new branch with the last character of alpha (split).
    3. If the last character of alpha exists, do nothing (implicit end).

The above inefficient algorithm works in O(m^3) time... but we can exploit some tricks to make it faster.

## Improving Time Complexity

Firstly, we can "get rid" of rule #1 by simply always keeping a pointer to the end of the string and extending it in each phase (end = end + 1). Remember that we store our string representations as numbers, such as [start, end]. This makes rule #1 trivial at each step and happens implicitly. Note that **each** node's end pointer grows by 1 at each step.

As soon as rule #3 is encountered, we can stop that phase since all subsequent suffixes are also contained in a path. Record the address at which you stopped so you can continue.

If you have stopped a phase by applying rule #3, you can continue the next phase from that point.

You can then go back and add $ characters by following the suffix links and applying rule #2 where necessary.

At the beginning of every phase, you can have a pointer to an address (node, edge, step) that is where you are currently at and can start the next phase from.