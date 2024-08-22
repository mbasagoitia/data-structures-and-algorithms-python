## Divide and Conquer Algorithm for Fast Fourier Transform

- Given a list of values, we need to represent them as a polynomial a0 + a1x + a2x^2 ... an/2x^n/2 ... + anx^n
- Divide this polynomial into two parts, aEven(x) and aOdd(x) each of length n/2
    - Assuming n is even, take (a0, a2x^2 + a4x^4 ... + an-2x^n-2) + (a1x + a3x^3 ... + an-1x^n-1)
    - The first part represents the even parts of the polynomial, and the second part the odd parts
    - Factor out an x from the aOdd function: x(a1 + a3x^2 ...)
    - Now we can express our polynomial as aEven(x^2) + aOdd(x^2)
    - **aEven(z)** = a0 + a2z ... + an-2 ... + z^n-2/2
    - **aOdd(z)** = a1 + a3z ... + an-1z^n-2/2
    - Where z = x^2
- A^i = aEven((wn^i)^2) + wn^i * aOdd((wn^i)^2)

*Interesting Fact*

If n is even and >= 2, (wn^i)^2 = (wn/2)^i

So, the ith Fourier Coefficient = aEven((wn/2)^i) + wn^i * aOdd((wn/2)^i)

If we can compute the even Fourier sequences and the odd Fourier sequences, then we can combine them to get the original Fourier sequence.

## Divide and Conquer

Basic idea:

- Split the list into two lists of length n/2, one of even coefficients and one of odd coefficients. *This assumes that n is divisble by two.*
- Calculate the FFT recursively on each half
- Combine results to get the kth element of the "final answer:"
    - If k < n/2, Ak = aEven(k) + wn^k + aOdd(k)
    - Else, Ak = Ak = aEven(k - n/2) + wn^k + aOdd(k - n/2)
- Base case: if n = 1 (list has length 1), the DFT is just itself, so return the list of one item.

What if n is odd or not a power of two?

There are other algorithms (such as FFT W by Cooley and Tuckey) that we can use but won't be discussed in this class.

## Time Complexity

T(n) = 2T(n/2) + O(n) <- dividing the problem into 2 n/2 problems and performing n element-wise additions of complex numbers

Using the master method, T(n) = O(n log(n))

The inverse FFT would be the same time complexity.