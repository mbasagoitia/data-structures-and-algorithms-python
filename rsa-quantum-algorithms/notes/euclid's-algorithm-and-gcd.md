# Euclid's Algorithm and GCD

For all integers m and n that are not 0, GCD(m, n) = GCD(n, m mod n)

Base case: if n = 0, return m (the last nonzero remainder)

## Time Complexity

Linear time complexity in the number of bits

Two numbers are relatively prime if their GCD is 1

# Bezout's Theorem

For any two integers m, n, there exist integers s, t (which can be positive or negative numbers) such that sm + tn = GCD(m, n). The integers s and t are known as Bezout coefficients.

If two numbers are relatively prime (GCD is 1), there exist integers s, t, such that sm + tn = 1