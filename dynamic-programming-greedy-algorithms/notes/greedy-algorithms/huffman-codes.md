# Huffman Codes

We want to find the optimal prefix code for ATCG.

Frequencies in the DNA string:

- A: 0.4
- C: 0.1
- T: 0.4
- G: 0.1

## Goal

Find a prefix code/tree such that the value of the tree (average bits per character) is minimized.

## Greedy Algorithm

1. Take the two least frequent characters (C and G in this case)
2. Form a composite character by combining them which has a frequency of the sum of the two characters' frequencies.

Now we have:

- A: 0.4
- T: 0.4
- [C, G]: 0.2

Where C and G form a subtree with paths 0 and 1

3. Repeat steps 1 and 2, with C and G "expanding out" from their place in the new subtree

- A: 0.4
- [T, [C, G]]: 0.6

4. Repeat until all characters are combined into a single tree/composite character.

- [A, [T, [C, G]]]: 1

Greedy criterion: At any point, take the two least frequent elements and combine them into a composite character with a new frequency which is their sum.

Now, you can calculate the bits/character, and this algorithm gives us the optimal minimum value.