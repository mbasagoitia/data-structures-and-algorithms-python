# Master Method and Solving Recurrences

In this section, we will focus on solving divide and conquer recurrences.

- You have an input of size n
- This input will be divided into a subparts of size n/b
- The values of a and b are dependent on the algorithm
- Obtain the outputs of each subproblem recursively, then combine them to form the final output

## Computing Time Complexity

- Time to divide the problem: fdiv(n)
- Time to combine the results: fcombine(n)

The recurrence is:

- T(n) = O(1) if n <= 1 (base case)
- aT(nb) + fdiv(n) + dcombine(n) if n > 1

- In merge sort, we divided our input into two parts of size n/2; a = 2, b = 2
    - fdiv(n) = O(1); fcombine(n) = O(n)
    - T(n) = O(1) if n <= 1
    - T(n) = 2T(n/2) + O(n) if n > 1

- In the max subarray problem, a = 2, b = 2, fdiv = O(1), fcombine = O(n)
    - Same recurrence as merge sort

- In Karatsuba's algorithm, n-bit number is divided into 2 n/2 bit numbers, and performed 3 multiplication subproblems. fdivide = O(n), fcombine = O(n)
    - T(n) = O(1) if n <= 1
    - T(n) = 3T(n/2) + O(n)

## Solving the Recurrence

### Expansion Method

Merge sort/max subarray example:

T(n) = 2T(n/2) + C1(n)
     = 2[2T(n/4) + C1(n/2)] + C1(n)
     = 2^2T(n/(2^2)) + 2C1(n/2) + C1(n)
     = 2^2T(n/(2^2)) + C1n + C1n
     = 2^2[2T(n/2^3) + C1(n/2^2)] + 2C1n
     = 2^3T(n/2^3) 2^2C1(n/2^2) + 2C1n
     = 2^3T(n/2^3) + 3C1n <- result of 3 expansions
     = 2^jT(n/2^j) + jC1n <- results of j expansions

What value must j be so that we reach the base case (n/2^j = 1)?
- n/2^j = 1
- j = log base 2 n; assume n is a power of 2 so that j is a whole number

T(n) = 2^log base 2 n * C0 + log base 2 n * C1n
     = C0n + C1 n log base 2 n
     = **O(n log(n))**

## Master Method

This method provides us with a "shortcut" to determine the recurrence

In the general case aT(n/b) + O(n^C):

epsilon = log base b a; we will compare this with c (work done in combine steps)

Three cases:

1. log base b a > c -> T(n) = O(n^(log base b a))
2. log base b a = c -> T(n) = O(n^(log base b a) * log n)
3. log base b a < c -> T(n) = O(n^c)

Merge sort solved with master method:

- a = 2, b = 2, c = 1 (because the work to combine is O(n) or O(n^1))
- log base b a = log base 2 2 = **1**
- c = **1**
- Case 2 applies; T(n) = n^1 * log n = **O(n log(n))**

Karatsuba:

T(n) = 3T(n/2) + O(n^1)
- a = 3, b = 2, c = 1
- log base 2 3 = 1.54....
- Case 1 applies; T(n) = O(n^1.54)

## Strassen Multiplication Algorithm

Multiplying 2 n by n matrices
- Divies the matrices into 4 n/2 by n/2 matrices
- Uses 7 multiplications to solve the problem
- T(n) = 7T(n/2) + O(n^2) because adding matrices takes n^2 time
- a = 7, b = 2, c = 2; log base 2 7 = 2.7....
- Case 1 applies; T(n) = O(n^2.7...)