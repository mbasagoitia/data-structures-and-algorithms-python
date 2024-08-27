# Longest Common Subsequence

Used in computational biology to align gene sequences

Given two strings s1 and s2 (not necessarily of the same length), find the longest possible subsequence (substring) that is common to both s1 and s2.

- s1 has length m
- s2 has length n
- We want to maximize the string that is a substring of both s1 and s2.

## Optimal Substructure

The LCS of a smaller part of each string contributes to the overall LCS of the entire length of both strings.

## Approach

Have a pointer i on the first substring and a pointer j on the second substring. 

3 choices:

1. Match the two characters where I am currently pointing (if s1[i] = s2[j])
    - 1 + BestMatch(i+1, j+1)
2. Advance i to i + 1 (no match at s1[i])
    - BestMatch(i+1, j)
3. Advance j to j + 1 (no match at s2[j])
    - BestMatch(i, j+1)

## Recurrence

lcs(i, j) where i represents the current suffix of s1 (pointer position until the end of the string, and j is for s2)

- Base cases: 0 when i >= m + 1, 0 when j >= n + 1 (no lcs when we go past the end of the substring)
- if s1[i] = s2[j]
        1 + lcs(i + 1, j + 1)
    else:
        max(lcs(i + 1, j), lcs(i, j + 1))
    
## Memoize

- Rows for i from i1 ... in+1
- Columns for j from j1 ... jn+1
- At some position i, j in the table, if the characters at that position are equal, look at i + 1, j + 1. Otherwise, either look at j + 1 or i + 1 and take the max of those two values.
- Need to fill in the table from right to left, bottom to top.

for i = m down to 1
    for j = n down to 1
        if s1[i] = s2[j]:
            LCS[i, j] = 1 + LCS[i + 1, j + 1]
        else:
            LCS[i, j] = max(LCS[i + 1, j], LCS[i, j + 1])

(this represents the beginning of the suffixes for each string)
return LCS[1, 1]

## Recover Solution

Have a table recording the annotation (1, 2 or 3) at each step. Each annotation corresponds to one of the recursive cases above. If it is a 1, move diagonally down and right (represents i + 1, j + 1). If it is 2, move down. If it is 3, move right. Each time you see a 1, count a match and record all matches in order, which will be the LCS.
