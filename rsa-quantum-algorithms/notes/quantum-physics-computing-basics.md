# Introduction to Quantum Computation

Computation and algorithms based on the principles of quantum physics

What is the relationship between computing and physics? From a high level to a low level, here is the flow:

- Algorithm runs in a high-level language such as Java or Python
- A virtual machine interprets and runs instructions on the CPU
- The CPU is made up of digital circuits with memory. These circuits are composed of 0s and 1s and AND, OR, NOT gates, flip flops
- Digital circuits are built on top of analog circuits (transistors, resistors, and other analog components) which push around charges--the 1 bit is interpreted as a high voltage and a 0 is interpreted as a low voltage used to charge a capacitor

In classical computation, concepts like 0s and 1s are reflected in physical states of matter (voltages/electrons moving around)

Conversely, quantum computing is based on the fundamental principles of quantum physics.

## Quantization

the idea that physical quantities can only have certain discrete values. Matter is quantized because it is made up of individual particles that cannot be divided. Electrons can only be in some discrete orbits around the nucleus, but not others.

## Heisenberg's Uncertainty Principle

A quantum system can exist in multiple states at the same time (such as an electron or photon). A quantum system can be described by a wave function, which tells you the probability of finding it in a particular state at a particular time.

Measurement (any kind of interaction) destroys the superposition--the superposition collapses to one state or the other. Superpositions are very hard to keep from collapsing.

## Stern-Gerlach Experiment

Individual atoms of silver were passed through an electromagnetic field. Each of these atoms behaves like a dipole; they are magnetized and have a direction. The angle of the dipole to the direction of the field influences its direction. What was found was two distinct intensities of where the silver atoms landed, and nothing in the middle. This suggests that magnetic moment is quantized--you can only have an up or down direction.

Taking a measurement along the "already filtered" z-direction of another instance of the experiment along the y-direction makes the orientation of the z-direction uncertain again.

## Main Ideas used in Quantum Computing

- Fundamental particles can be in multiple states at the same time (directions, magnetic moments, etc) called superposition of states.

- Measurement (or any type of interaction) causes the superposition to partially or fully collapse. When this happens, you get a definite state.

- Entanglement (we will explore more later)

- Quantum parallelism and influencing probability of measuring the correct answer