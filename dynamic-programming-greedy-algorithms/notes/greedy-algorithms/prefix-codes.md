# Prefix Codes

Related to non-lossy file compression (e.g. zip). Characters must be encoded to 8-bit sequences to be stored on a disk.

- Read more about ASCII (American Standard Code for Information Interchange)

Compressing a file makes it into a much smaller version that can be expanded back again to the orignal file.

One strategy may be to encode common characters with fewer numbers of bits to take up less disk space, but this makes encoding difficult because of varying bit lengths. We can avoid this complication by using a **prefix code.**

We must find a way to have exactly one way to decode a string.

- No character's code may be the proper prefix of another character's code.

Example:

- A: 0
- C: 10
- T: 110
- G: 111

None of these codes are a proper prefix of another, so there is only one way to decode the resulting encoded string.

## Prefix Trees

Prefix codes can be written as trees, reading from the root node to the leaves.

We may know the frequency/weight of each character's occurrence and calculate bits per character for each prefix tree. We want to minimize average bits per character, which is calculated as the sum of each character's depth times its weight. Such a minimized code is called the optimal prefix code.