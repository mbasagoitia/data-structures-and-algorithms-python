# Order Finding and Factoring

## Shor's Algorithm

Algorithm for factoring semiprime numbers of the form N = pq. Uses an operation called order finding

Steps:

- Choose sum random number a that is relatively prime with N. Consider powers of a % N until you find a cycle such that a^i % N = a^i + j % N. We know that a^j % N = 1.

The order r of a is defined as the smallest number r > 0 such that a^r % N = 1. Suppose that the order r of a is an even number and t is r/2. We can say that (a^t + 1)(a^t - 1) % N = 0. If GCD(a^t + 1, N) is not 0, we have found a factor p or q.

From the above steps, the following two things need to happen (but are not guaranteed to be true) in order to find a factor:

- r is even
- a^t + 1 % N != 0

The difficult part about this part of the algorithm is finding the order r quickly. However, with quantum algorithms, r can be found in polynomial time.