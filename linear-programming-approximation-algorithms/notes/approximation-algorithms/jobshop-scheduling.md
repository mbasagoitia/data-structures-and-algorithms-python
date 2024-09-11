# Jobshop Scheduling and Algorithm Design

Given a list of n tasks where T[i] represents the time taken for each task/job and m processors where each job can be done by one of the processors, find an assignment A[i] = j where i goes from 1 ... n and j goes from 1 ... m, and the makespan is the maximum load given to any processor (time for all processors to finish all jobs), determine the minimum makespan.

For each processor, the load is the sum of the time of all tasks assigned to it.

This is an NP-hard problem and NP-complete (reduces from partition problem).

## Greedy Scheduling

Go through each job one by one, where T[i] represents the time for the current job being scheduled and J[i] represents the time commitment for jobs already assigned to that processor. This algorithm finds the min value for J[i] (processor with the lightest load) and assign the current job to it. 

A = [None ... None] (initial processor assignments of None) for all 1 ... n

J = [0 ... 0] for all 1 ... m (initial total load for each processor)

for i = 1 to n:
    k = indexOf(min(J)) (heap/priority queue)
    A[i] = k
    J[k] = J[k] + T[i] (maintain heap)

Runs in O(n log(m)) if you use a priority queue. The greedy algorithm doesn't always match the optimal solution, but is bounded by a factor of 2 compared to the optimum.