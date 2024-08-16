# Karatsuba's Algorithm

Multiplication algorithm for large numbers

Your computer can only multiply 2 64-bit numbers at a time, so we want to be able to multiply much larger numbers

Uses in cryptography, RSA

Many language carry this "under the hood," but we will look at that algorithm here.

## Adding together two bit arrays A and B of size n into an array C of size n + 1:
def add_bit_arrays(A, B):
    n = len(A)  # Assuming A and B are the same length
    C = [0] * (n + 1)  # Initialize result array with size n+1 (to accommodate overflow)
    carry = 0
    
    for i in range(n):
        C[i], carry = sum_of_bits(A[i], B[i], carry)
    
    C[n] = carry  # Final carry
    
    return C


def sum_of_bits(a, b, carry):
    # Compute the sum bit and new carry
    sum_ = (a + b + carry) % 2  # Sum bit (equivalent to XOR)
    new_carry = (a + b + carry) // 2  # New carry (equivalent to AND and OR)
    return (sum_, new_carry)

def sum_of_bits_bitwise(a, b, carry):
    # Calculate sum and new carry
    sum_ = a ^ b ^ carry  # XOR to get the sum bit
    new_carry = (a & b) | (carry & (a ^ b))  # AND & OR to get the new carry
    return (sum_, new_carry)


## Multiplying Large Numbers

### Grade school algorithm

Given two arrays A and B of lengths n and m respectively, the product C of A and B will be an array of length m + n.

We will need these two operations:

add_to(res, x):
    res = res + x

shift_left(res):
    res = res + [0]

multiply(a, b):
    res = [0....0] length m + n
    # temp array to save shifted version of A
    temp = a
    for j = m down to 1:
        if b[j] == 1:
            add_to(result, temp) # We already defined the add_bit_arrays function above...use that!
        shift_left(temp)

Explanation: the shift left occurs regardless of whether the current bit in B is 0 or 1, but the addition of the entire temp array (initially A) happens only if the bit is 1, because multiplying something by a 0 bit is 0.

The time complexity of this operation is O(n^2). Let's do it better!

## Divide and Conquer Approach

Divide and conquer approach for multiplication of large numbers

Given two bit arrays a and b, each of length n where n is a power of 2, multiply them.

- Split both arrays down the middle so you have n/2 elements in each half: [a1], [a2], and [b1], [b2]
- [a] = 2^[n/2][a1] + [a2]
- [b] = 2^[n/2][b1] + [b2]
- Recall that multiplying a binary number by 2^2 simply adds two zeros to the end
- So, multiplying a number a by 2^k means adding k zeroes to the end of a
- [a] * [b] = 2^n[a1]*[b1] + 2^n/2[a1][b2] + [a2][b1] + [a2][b2]

multiply(a, b):
    if len(a) and len(b) == 1
        one_bit_multiply(a, b)
    else:
        split a into a1 and a2 and b into b1 and b2 of size n/2
        r1 = multiply(a1, b1)
        r2 = multiply(a1, b2)
        r3 = multiply(a2, b1)
        r4 = multiply(a2, b2)
        r1 = pad(r1, n)
        add(r2, r3)
        pad(r4, n/2)
        add(r1, r4, r5)

To multiply n bit numbers, you have to carry out 4 n/2 bit multiplications, 1 n bit padding, 1 n/2 bit padding, 1 n bit addition, and 2 2n bit additions

Recurrence: T(n) = O(1) if n = 1; T(n) = 4T(n/2) + O(n) if n > 1
When solved, this is O(n^2)

This is the exact same as grade school algorithm!

## Karatsuba's Algorithm

1. Divide `a` and `b` into two halves: `[a1]`, `[a2]` and `[b1]`, `[b2]`.
2. Compute three products:
   - `r1 = [a1] * [b1]`
   - `r2 = [a2] * [b2]`
   - `r3 = ([a1] + [a2]) * ([b1] + [b2])`
3. Calculate the middle term:
   - `r_middle = r3 - r1 - r2`
4. Combine the results:
   - `r = r1 * 2^n + r_middle * 2^(n/2) + r2`
   - Where n is the total number of bits in the original numbers.
5. Complexity:
   - The new recurrence relation is `T(n) = 3 T(n/2) + O(n)`
   - When solved, this yields a time complexity of `O(n^1.54)`
