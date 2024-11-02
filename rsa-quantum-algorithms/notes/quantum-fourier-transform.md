# Quantum Fourier Transform

The FT is good at finding the period of periodic functions and will yield peaks at multiples of M/r.

The quantum algorithm attempts to find the period  𝑟  of the function  𝑓𝑎,𝑛(𝑗)=𝑎𝑗mod𝑛 . 

We now perform a quantum fourier transform on the superposition we got as a result of the first step of the algorithm, which gives us r.

After measuring the state after QFT, we get a result that is some multiple C * M/r. We can extract r from this using a continued fraction method.

(November 1 screenshot)

Remember that r has to be even and some other factors have to hold to find a factor p or q.

Recall that the DFT of a sequence of complex numbers [a0, a1, ... aM-1] yields the fourier coefficients [A0, A1, ... AM-1] where

Aj = p(wM^j). Recall that the polynomial p is a polynomial representation of the original coefficients of the form a0 + a1x + a2x^2 ... + aM-1^M-1.

### Quantum Analog of DFT

Suppose you are given a state of a quantum system in a superposition a0 |0...0> + a1 |0...1> ... + aM-1 |111...M-1>. Each ket value is a number of M bits. Applying QFT to this superposition yields another superposition written as summation from j = 0 to M - 1 of Aj |j>, where j is the jth fourier coefficient. j itself is a binary string jm-1 ... j0.

The QFT is a unitary operator.

The QFT takes a divide and conquer approach based on whether or not jm-1 ... j0 is odd or even (consider the last bit of the binary string).

Think of the higher order bits as j' (all bits except the last one representing the 1 slot) and the 1 slot as j0.

We can now write the QFT as summation from j = 0 to M - 1 of Aj |j'> x |j0>. We further separate this out into two superpositions:

- Summation from j = 0 to M/2 - 1 of Aj' |j'> x |0>
+
- Summation from j = 0 to M/2 - 1 of Aj' |j'> x |1>

AKA |fi even> |0> + |fi odd> |1>

Where fi even are terms where j0 = 0 and fi odd are terms where j0 = 1

Feed j' (all bits except j0) into QFT M/2, and j0 comes along for the ride but is entangled with bits of j'.

Now we have QFT M/2 (|even> x |0>) + QFT M/2 (|odd> x |1>)

Unlike in FFT where we did the two steps separately and then combined them in divide and conquer, in QFT, these operations are done by the same QFT circuit, which gives us an exponential speed up from FFT.

In the combine step, all m bits come through in reverse order (LSB and MSB are flipped) to form the superposition QFT M/2 (|even> x |0>) + QFT M/2 (|odd> x |1>)

We need to get to the following superposition:

Summation from k' = 0 to k' = M/2 - 1 (Ek' + wm^k' * Ok') |k'> |0> + summation from k' = 0 to k' = M/2 - 1 (Ek' - wm^k' * Ok') |k'> |1> where E is even and O is odd, where either + or - is determined by the MSB.

To achieve this, we need to perform a unitary operation. By factoring out terms and seeing what they need to transform into, we get the following:

- |0> -> |0> + |1>
- |1> -> wm^k' |0> - wm^k' |1>

The unitary operation Uc (U combine) looks like this: H x [1 0]
                                                          [0 wm^k']

Which is the Hadamard gate combined with a controlled phase matrix of phase wm^k'

And wm^k' = e(^2 pi i k0)/2^m, e(^2 pi i k1)/2^m-1, ... 

Where k' is the binary number [km-2 ... k0] whose value is 2^m-2km - 1 ... 2^0k0 (value of k)

The phase is applied if k0 ... km-2 is 1. The phase is 2pi/2^m

At each step, the circuit is only applying single qubit gates like H or CP (Hadamard and controlled phase gate). It recursively applies the QFT to about 2 qubits at a time for a total of m^2 gates.