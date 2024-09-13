# Approximation Algorithms for MAX 3-SAT problem

Recall that the MAX SAT problem involves n true/false variable and m clauses with (in this case 3) literals, the clauses being ANDs of ORs and the literals can be negated or not.

The goal is to find the truth assignment for each decision variable that satisfies the maximum number of clauses. This problem is NP-complete. We can implement it as an integer linear program. Here, we will explore approximation algorithms.

## Approximation Algorithm

This approximation yields a solution of a factor no worse (smaller) than 7/8 of the optimum solution.