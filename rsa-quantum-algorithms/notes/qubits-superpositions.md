# Qubits and Superpositions

A qubit is a unit of quantum information--the quantum bit.

In classical computing, a bit can be a 0 or a 1 that is mapped to a state of physical matter.

In quantum computing, 0 and 1 map to an orientation or spin (up/down) of an electron, magnetization of a dipole in one direction or the other, polarization of a photon (clockwise, circular, etc.), etc.

We describe states of matter in terms of wave functions in the quantum world. The state of a quantum system can be written in ket vector notation: | 0 >

Pure states: an electron's spin or polarization can be purely up or down, etc. If something is a 1 or 0, it cannot be the other.

This contrasts with the idea of a quantum system being in a superposition of pure states. Written as a|0> + b|1>, where a and b are complex numbers that are called amplitudes.

When you measure a superposition, you get a probability given by the amplitude |a|^2, or the complex number a written as A + Bi, sqrt(A^2 + B^2) that the superposition collapses into 0, or with probability |b|^2 it collapses to 1. Therefore, one of the properties of a superposition is that **a^2 + b^2 = 1** because probabilities must add up to 1.

Remember that measuring collapses the superposition. If you get a 0, measuring it again will always cause you to measure a 0 no matter the original probability.

## Quantum Operations

Quantum mechanical operators are described by unitary matrices and transform one superposition into another.

Unitary operations: Manipulates a and b with a special matrix known as a unitary matrix U (a 2x2 matrix of complex numbers), which creates a new superposition given by U * a b, which gives you a'|0> and b'|1> (U applied to a|0> + b|1>)

A unitary matrix is unitary if U+ (the transposed matrix with each element's complex conjugate applied) * U = U * U+ = I (identity matrix), in other words U and U+ are inverse

When you create a new superposition by applying a unitary matrix to a and b, the squares of the sum of a' and b' must still equal one. This is necessary for the superposition to be valid.

Two vectors are orthogonal (perpendicular) if their dot product is 0. |0> and |1> are orthogonal.

## Unitary Operators and Reversible Computation

Quantum operations are reversible. If you apply a unitary operation U to a and get a', you can apply U+ to a' and get a.

The only operation that is not reversible is measurement.

Hadamard Gate: 1/sqrt(2)[1, 1]
                        [1, -1]

The Hadamard Gate transforms |0> and |1> into a superposition of 0 and 1 with equal probability of measuring each.

|0> -> Hadamard Gate -> 1/sqrt(2) (|0> + |1>)

|1> -> Hadamard Gate -> 1/sqrt(2) (|0> - |1>)

The Hadamard Gate is its own inverse (its own U+)

X-Gate (quantum NOT): [0, 1]
                      [1, 0]

The X-Gate transforms |1> into |0> and |0> into |1> and is also its own inverse (U+)

Phase Operator: [1, 0]
                [0 e^i*fi]

Turns |0> into |0> and |1> into e^i*fi |1> (applies a phase to the amplitude of the |1>)

The inverse of the phase operator is  [1, 0]
                                      [0 e^-i*fi]

