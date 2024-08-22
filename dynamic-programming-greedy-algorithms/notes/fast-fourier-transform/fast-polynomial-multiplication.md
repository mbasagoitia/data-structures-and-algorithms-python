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