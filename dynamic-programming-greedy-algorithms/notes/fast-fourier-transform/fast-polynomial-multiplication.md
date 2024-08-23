# Fast Polynomial Multiplication with FFT

Given two sequences of n numbers that represent polynomials of degree n-1,

a = [a0 ... bn-1]
b = [b0 ... bn-1]

find the product a(x) * b(x)

The product C will have degree 2n-2

If you take the FFT of a and b (padding them with 0s since C will have more coefficients than A or B), C0 = A0 * B0 and Cn-2 = An-2 * Bn-2, so we have the FFT coefficients of C.

Take the inverse FFT of C's coefficients to get the polynomial.

## Summary

- Extend the sequences to the next power of 2 (pad with 0s)
- Compute the FFT for each sequence
- Multiply the resulting FFT sequences element-wise
- Apply the inverse FFT to get the coefficients of the product polynomial

## Time Complexity

O(n log(n)) vs the naive algorithm which gives you O(n^2) time

## From the Textbook

The following procedure takes advantage of the FFT to multiply two polynomials A.x/ and B.x/ of degree-bound n in ‚.n lg n/-time, where the input and
output representations are in coefûcient form. The procedure assumes that n is an
exact power of 2, so if it isn’t, just add high-order zero coefûcients.

1. Double degree-bound: Create coefûcient representations of A.x/ and B.x/ as
degree-bound 2n polynomials by adding n high-order zero coefûcients to each.
884 Chapter 30 Polynomials and the FFT

2. Evaluate: Compute point-value representations of A.x/ and B.x/ of length 2n
by applying the FFT of order 2n on each polynomial. These representations
contain the values of the two polynomials at the .2n/th roots of unity.

3. Pointwise multiply: Compute a point-value representation for the polynomial
C.x/ D A.x/B.x/ by multiplying these values together pointwise. This representation contains the value of C.x/ at each .2n/th root of unity.

4. Interpolate: Create the coefûcient representation of the polynomial C.x/ by
applying the FFT on 2n point-value pairs to compute the inverse DFT.
Steps (1) and (3) take ‚.n/ time, and steps (2) and (4) take ‚.n lg n/ time.