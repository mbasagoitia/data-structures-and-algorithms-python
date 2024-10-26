# Multiplie Qubit Quantum States

It is possible to have multiple qubits that are a part of the same system. They are each described by their own amplitudes. Their direct or tensor product can be described by the cross notation and is a linear combination of the probabilities of their amplitudes (distribute like normal). The tensor product describes **separable** (not entangled) states in the same system.

In general, when computing the tensor product, a x b != b x a

In a 2 qubit system, the pure states and orthogonal basis states are |00>, |01>, |10>, |11>
- 2^n such pure states exist for a system with n qubits

The same principle holds that the squares of the complex amplitudes of each basis state (probabilities) must add up to 1.

## Entangled States

Bell/EPR State: 1/sqrt(2) (|00> + |11>)

Two bits: b1 and b2 in a joined superposition where they will collapse to either 00 or 11; they cannot be different. The Bell state (and all other entangled states) cannot be written as a tensor product of two individual quantum states.

## Partial Measurement

Imagine you have prepared two qubits in a Bell state. If you measure only one of them, it collapses to 0 with probability 1/2 and to 1 with probability 1/2. However, as soon as one qubit is measured, the second also collapses to the stame state as the first. It is predetermined in a sense. They are in an entangled state.

## Multi Qubit Quantum Gates

Suppose you have a 2 qubit system |00> and perform the Hadamard gate on the first qubit and the identity matrix on the second (do nothing).

This is equivalent to H x I = 1/sqrt(2) * (|0> + |1>) x |0> = 1/sqrt(2) * (|00> + |10>)

Applying the Hadamard gate to both qubits gives you 1/sqrt(2) * (|0> + |1>) x 1/sqrt(2) * (|0> + |1>), which simplifies to
1/2*(|00> + |01> + |10> + |11>) (uniform superposition)

Remember that the Hadamard gate operation is the matrix [1/sqrt(2), 1/sqrt(2)]
                                                        [1/sqrt(2), -1/sqrt(2)]

And the identity matrix is [1, 0]
                           [0, 1]

A unitary operator U acting on an n qubit system will be a 2^n x 2^n matrix.

When multiple gates act independently on separate qubits, their combined operation is represented by the tensor product of their matrices.

## Controlled Single Qubit Operators

You may have a control qubit and a qubit you are operating on. If the control qubit q1 is in state |1> then q2 is transformed by U. If q1 is in state |0>, then q2 remains the same. In either case, q1 remains the same.

## Controlled NOT Gate

q1 is control qubit and q2 is target qubit. 

If q1 is 0, q2 is unchanged. If q1 is 1, then q2 is transformed to the opposite state. U is a 4x4 matrix for this operation, given by [I 0]
   [0 X]

Where I = identity matrix and X = NOT. Remember that each of these four values in the matrix are each a 2x2 matrix (gate) represented by 1s and 0s.

## Controlled Hadamard Gate

Say that q2 is the control this time and q1 is the target. If q2 = 1, then Hadamard gate is applied to q1.

|01> = H|0> x |1> (tensor product of Hadamard |0> and |1>) = 1/sqrt(2)(|01> + |11>)

## Multi-Control Gates

- CCX, where you have two control qubits and one target qubit. If q0 and q1 both = 1, then q2 is operated on with X (flipped), else q2 remains q1 (operated on by I). Since this is a 3-qubit operation, it will be an 8x8 matrix.

The Bell state can be created by starting with two qubits q1 and q2, and performing H on the first bit and then CNOT on the second bit.

## Creating Uniform Superposition

It is standard to assume that all qubits are initialized to |0> before beginning any computation. To create a uniform superposition, apply H to each bit individually.