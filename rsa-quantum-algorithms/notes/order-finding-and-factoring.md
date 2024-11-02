# Shor's Algorithm

Algorithm for factoring RSA numbers

You can factor n, the product of two large prime numbers p and q, in **polynomial time** on a quantum computer.

Algorithm for factoring semiprime numbers of the form N = pq. Uses an operation called order finding

## Order Finding and Factoring

Steps:

- Choose sum random number a that is relatively prime with N. Consider powers of a % N until you find a cycle such that a^i % N = a^i + j % N. We know that a^j % N = 1.

The order r of a is defined as the smallest number r > 0 such that a^r % N = 1. Suppose that the order r of a is an even number and t is r/2. We can say that (a^t + 1)(a^t - 1) % N = 0. If GCD(a^t + 1, N) is not 0, we have found a factor p or q.

From the above steps, the following two things need to happen (but are not guaranteed to be true) in order to find a factor:

- r is even
- a^t + 1 % N != 0

The difficult part about this part of the algorithm is finding the order r quickly. However, with quantum algorithms, r can be found in polynomial time.

Steps:

Choose a random  𝑎∈[2,𝑛−1] . If  𝐺𝐶𝐷(𝑎,𝑛)≠1  then we have found our prime factor!
(Assume  𝐺𝐶𝐷(𝑎,𝑛)=1 ). Use quantum computer to find the order  𝑟  of  𝑎  modulo  𝑛 .
If  𝑟  is even and  𝑎𝑟/2+1mod𝑛≠0 :
Computing  𝐺𝐶𝐷(𝑎𝑟/2−1,𝑛)  will yield a factor of  𝑛 .
If condition in previous step fails, repeat step 1.

## Order Finding on a Quantum Computer

A unitary operation U operates on j (a number of m bits) to produce f(j), which is a periodic function where r is the period (cycle that repeats where some value a^r % N is 1).

The unitary function "knows" what N and a are and we don't need to provide them as inputs.
f(j) = a^j % N

First, we prepare a result register of m bits.

For all m bits of the input j, apply the Hadamard gate to each one to get a uniform superposition of all 2^m combinations.

U runs through all possible combinations of states * a ^ 0 ... a ^ M - 1 % N

In other words, it is the sum from j = 0 -> j = 2^(m - 1) ket j x (f(j)) (including the normalization factor).

Then, a partial measurement of the result register is performed. The result register collapses to some value k.

The original qubits will also collapse when this happens and yield some value x0 + alpha * r, which represents some x0 and some multiple of r in the periodic function. But we don't know what x0 is!

So, how do we figure out r?

Apply the QFT