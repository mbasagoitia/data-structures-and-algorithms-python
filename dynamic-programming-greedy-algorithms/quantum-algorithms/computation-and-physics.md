# Computation and Physics

Quantum algorithms run on quantum computers, which are based on the principles of quantum physics.

First, let's understand "classical" computers:

- Programming languages are compiled into machine instructions that run on the CPU and memory
- Inside of the CPU are a series of logic gates (and, or, not) that manipulate 1s and 0s
    - 1 corresponds to a voltage level above some certain threshold, and 0 is a voltage level below some certain threshold
- Therefore, we map pieces of information to physical states (voltage)
- Memory: RAM: capacitor that stores a charge. Memory storage is achieved by changing the state of physical systems (magnetization, charge)

Overall, we are controlling the motion of electrons inside the integrated circuit (current).

## Classical vs. Quantum Physics

Classical physics is based on the discoveries of Newton, Maxwell's equations, etc. 

- Electrons, protons, neutrons
- Light (wave, not particle)
- Length, energy, momentum, etc. exist on a continuum (0 -> infinity)

Discrepancies:

- Spectrum of elements like hydrogen
    - Didn't observe continuous radiation in spectral lines; rather, only emission at certain wavelengths

- Photoelectric effect: some materials generate a voltage when light falls on it; creates voltage potential (electricity), which depends upon the frequency of the light wavelength (unexpected).

This all led to the quantum hypothesis: 

Energy or light is emitted/absorbed in packets/quanta. Light is a "particle" (photon). Electrons will behave like waves (double-slit experiment) and form a diffraction pattern. When you observe this happening, that pattern goes away!

Duality in matter: waves and particles are interchangeable dual states of matter.

Uncertainty Principle: When you try to measure something like an electron (shine light on it), it moves the electron in an unpredictable manner and you cannot measure its velocity. If you try to measure its velocity, you can no longer accurately measure its position.

At the deepsest levels of matter, things like position and velocity are inherently uncertain (random).

Quantum physics says that things (subatomic particles) can "exist" in mulitple possible states at the same time.

## Quantum Information

Instead of bits of 0s and 1s, we have qubits which can be 0 or 1. Where bits are mapped to physical states (voltages), quibits can also be mapped to physicals states (electron spin-up, spin-down, polarization) known as pure states. This allows for superpositions: a qubit can be both 0 and 1 at the same time. When measured, the uncertainty collapses and with probability 1/2 becomes either a 0 or a 1. This parallelism can be exploited in very interesting ways.