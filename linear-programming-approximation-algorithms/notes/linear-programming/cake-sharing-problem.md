# Cake-Sharing Problem

An introduction to linear program modeling

- 3 people: Alice, Bob, Charlie
- 1 cake

Constraints:
- Alice wants at least as much cake as Bob
- Bob wants at least twice as much cake as Charlie
- Charlie wants at least 1/10th of the cake
- Bob's doctor wants Bob to have no more than 1/2 the cake

- Alice offers to pay money to charity for the cake; if you give her the whole thing, she gives you $10; half, $5, quarter, $2.50, etc.
- Bob offers to pay $12 and associated fractions
- Charlie: $15 and associated fractions

Our goal: divide the cake between the three people, making sure that we maximize the amount that goes to charity while respecting these constraints.

## Modeling the Problem

Decision variables
- xA = fraction of cake that goes to Alice
- xB = fraction of cake that goes to Bob
- xC = fraction of cake that goes to Charlie

Total amount of money going to charity: 10xA + 12xB + 15xC

We need to maximize this function: 10xA + 12xB + 15xC

Constraints
- xA >= xB
- xB >= 2xC
- xC >= 1/10
- xB <= 1/2
- xA + xB + xC = 1
- xA, xB, xC >= 0
- xA, xB, xC <= 1

We can guess values to find a feasible solution: xA, xB = 2/5; xC = 1/5 which gives us $11.80 to charity

In future lessons, we will learn how to solve algorithms like this with algorithms and packages rather than just guessing.