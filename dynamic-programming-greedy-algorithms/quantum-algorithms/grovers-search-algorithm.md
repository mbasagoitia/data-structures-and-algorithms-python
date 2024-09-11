# Grover's Search Algorithm

Demonstrates how quantum computing can achieve speed-ups.

Given a classical digital circuit (with AND, OR, and NOT gates) over n inputs, an output, and a black box function, find an input to make the output 1.

This is similar to the SAT problem.

In classical computation, the best known algorithm has 2^n time complexity. It runs through all possibilities. We will see how Grover's Algorithm can achieve 2^n/2 time complexity.

Because quantum algorithms are fundamentally randomized, it will give you the wrong answer some of the time, with very low probability. However, the probability of repeatedly getting the wrong answer is negligibly small.

We will take our function f with an n-bit input and a 1-bit output and make it a quantum function--it will operate on qubits. Remember, operations must be unitary--AND and OR are not unitary (and they are not invertible), but NOT is.

## Quantum Version of the AND Gate

Instead of two inputs to AND, have three: the original qubits plus a result qubit, set as 0. q1 and q2 (original qubits remain unchanged), and the result bit (the last bit in the sequence) stores the result. This makes the process invertible by preserving the original state. Now it is a unitary operation!

The same can be applied to classical NOT to make it work in quantum computing.

As a result of this, any classical circuit can be implemented as a quantum version.

The single circuit computes in parallel the resut for all configurations of the bits.

## Grover's Search Algorithm

Given a classical box f with n inputs and one output, we will make a quantum version of it. Every time we run f, we need to prepare intermediate result registers, which are 0.

Our n inputs are 0 ... 2^n-1 represented in binary.

Initialize a vector u as a sum of all n-bit numbers. There are 2^n of them.

If u is a bit of 000 ... 000, apply the Hademard Gate to every bit. 

Theta is the angle made between u and ei. Dot product of u and ei gives you the cosine of the angle.

u = 1/2^n(000 .... 111) uniform vector

ei = 1/2^n-1 (000 .... i-1, i+1, 111) <- notice that i is missing.

We want to rotate a vector w (starts at u) towards i by 2 theta radians (we don't know i). We can solve for how many rotations we need to reach i (theta * sqrt(2^n)). Then, measure w and return the answer, which with very high probability will collapse to i.

## How to Rotate

- Reflect wj about ei, which is wj*
- Reflect wj* about u to get wj+1

The angle between wj and wj+1 is 2 theta.

Reflection is a unitary operation we can do in quantum mechanics

theta * sqrt(2^n) operations gets you very close to the result i, which you can then measure and have a high probability of yielding the correct answer.

# Shore's Algorithm

Used for factoring RSA numbers.

Given a number n which is the product of two prime factors p and q, you can find the factors in polynomial time, but only on a quantum computer!

