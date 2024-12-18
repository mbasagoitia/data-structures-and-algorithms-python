# Grover's Search Algorithm

Given a digital (classical) circuit over n inputs (black box function) and a 1-bit output, find an input that makes the output 1. This is equivalent to the SAT problem. The best known classical algorithm to solve this problem has 2^n time complexity.

The quantum algorithm runs in 2^(n/2) time. Because quantum computation is fundamentally randomized, the output of the algorithm will be a value that makes the function true with high probability, or possibly a different output with very low probability.

Steps of the algorithm:

1. Make the black box function a quantum function--we need to operate on qubits and have unitary operations (remember that AND and OR are not unitary). NOT gate works in quantum computing. You can implement AND and OR as unitary operations by having a result qubit (see previous lectures). This will require preparing a number of intermediate result register bits.

2. Initialize a vector u that is the sum of all 2^n bits with normalization factor 1/sqrt(2^n). Imagine a space where ei (all solutions except the correct one, i) is the x-axis and i (the correct answer) is the y-axis.

3. Prepare another vector w0 = u

4. For j = 1 ... k steps, where k = pi/4 * sqrt(2^n), rotate wi + i by 2 theta radians by applying reflections (unitary operations).
    1. Reflect wj about ei
    This is done by running all values through the black box function and negating the value whose result register is 1, which only the correct solution will be

    2. Reflect wj hat about u, yielding wj+1
    This is done by applying change of basis of u to a vector of all 0s, reflecting it about u, and change of basis back to u. In other words, Hadamard -> negate all but one bit -> Hadamard

After these reflections, the angle between wj and wj+1 = 2 theta (towards an unknown value i).

Perform sqrt(2^n) of these operations and you will get very close to the result.

5. Measure w and return answer


When you run your inputs against the quantum version of the black box function, all possible states are computed in parallel.