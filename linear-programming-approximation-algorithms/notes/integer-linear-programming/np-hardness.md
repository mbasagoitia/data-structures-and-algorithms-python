# NP-Hardness of Integer Linear Programming

An NP-complete problem is a type of computational problem that has two key characteristics:

In NP: The problem is in the class NP (nondeterministic polynomial time), meaning that if you are given a candidate solution, you can verify whether it is correct in polynomial time. In other words, you can quickly check if a solution is valid, even if finding the solution itself might be difficult.

NP-hard: The problem is as hard as any problem in NP. This means that every problem in NP can be transformed, or "reduced," into this problem in polynomial time. If you could solve this NP-complete problem efficiently (in polynomial time), you could solve every problem in NP efficiently.

## 3-SAT

- Has some propositions P1 ... Pn that are true/false
- Contains m clauses c with 3 literals each which is either a proposition or its negation

We want to find out if there is a truth valuation for each proposition that satisfies every one of the clauses

## Reducing 3-SAT to a Binary ILP Problem

Decision variables:

- x1 ... xn where xi = pi and is 0 or 1 (false or true) <- indicator variable
- t1 ... tm where tj = 0 or 1 (cj, each clause is either satisfied or not satisfied)

Objective: maximize t1 + t2 ... + tm (number of clauses satisfied)

Constraints:

Example of 1 clause below, but applies to all clauses

Clause: (P1 or P3 or P*7) where P* = negation

- Constraint: x1 + x3 + (1-x7) >= t1
    - We want t1, our indicator variable, to be true/satisfied
    - The only way t1 can be 1 is if at least one of the variables x1, x3, or x7 is 1

Next clause: (P3 or P8 or P*4)

- Constraint: (x3 + x8 + 1-x4) >= 1

Once all clauses have been translated into constraints, we ask "is there an objective value that is >= m?"

Solving an integer linear program is not known to be polynomial time, whereas solving a linear program is.

## LP

Algorithms like Simplex, Interior Point, Ellipsoidal that can solve LP problems in polynomial time.

## ILP

NP-Complete and NP-Hard -- no known polynomial time algorithm. There are exponential time algorithms.