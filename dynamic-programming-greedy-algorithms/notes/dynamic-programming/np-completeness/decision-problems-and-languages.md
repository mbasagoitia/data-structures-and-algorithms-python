# Decision Problems and Languages

Related to the Theory of Computation and inherent difficulty of solving problems.

## Why Study Decision Problems?

- The size of the answer is just 1 bit
- Language: the set of all inputs which gives us the yes answer
    - For example, prime is the set of all numbers which would give us "yes" to the question "is this a prime number?"
    - This language contains {10, 11, 101, 111 ...} (in binary form) <- language
    - Another example: path is a language that is the set of all graphs with source s and destination t such that G encodes a graph where s is connected to t. This language is encoded as a binary string.

## How Do We Define a Problem?

Optimization problems can often be expressed as a related decision problem.

A problem is defined by a language -- choosing certain binary strings which have some meaning. An algorithm can therefore be defined as a "box" which, given an input string x, tells you if x belongs to a language. This algorithm recognizes language l.

Church-Turing Thesis: Turing Machines are a universal model of computation. Anything we can compute using a physical device that can carry out any form of computation is equivalent to a Turing Machine.

There is a boundary between problems that can be solved on a computer (decidable problems) and problems that cannot be solved on a computer (undecidable problems).

Examples of undecidable problems:

- Halting problem: Given a program, determine if it has an infinite loop.
- Diophantine equation problem: Given a diaphantine polynomial (all coefficients are integers), are there integer assignments to the variables that solves the equation?
    - There is no algorithm for a general solution.

In the realm of decidable problems, there are problems that can be solved fast and those that cannot, due to fundamental limitations in math, computing, etc.