# Qubits and Quantum Operations

- Pure states of 0 and 1; electron bit spin up/down; photon polarization
- Superposition states of 0 and 1 can exist; collapses to either 0 or 1 with probability 1/2
- Coefficients of the state (0 or 1) are complex vectors in the Hilbert space and the modulus of the state is the sum of the modulus of the individual elements

## Basic Idea in Quantum Computing

Prepare qubits and run some quantum operations on them, then do a measurement to get an answer.

In a quantum system with multiple qubits, you have several bits in different states; these states can be in multiple qubits. When measured, the system collapses to a pure state n with alpha n ^ 2 probability.

Entangled vs. non-entangled states: measuring b1 also causes the collapse of b2 in an entangled state; if not affected, it is non-entangled.

Partially-entangled states

## Operations on Qubits

We can measure qubits. If you have a system of k qubits and measure one, you can measure all of them at a time. They either collapse or remain in a superposition state.

Quantum operations are a form of linear transform; manipulate the probabilities of being 0 or 1. The operator cannot change the amplitude of the state; alpha 1 ^ 2 + alpha 2 ^ 2 must always equal 1.

Any quantum operation other than measurement must be reversible.

Operators must be unitary.

Operators:

- Quantum NOT: inverts the qubit from 1 -> 0 or 0 -> 1. Has a matrix representation. "Flips" the probabilities.
- Hademard Gate
- Rotation by theta
- Reflection of a quantum state around a vector