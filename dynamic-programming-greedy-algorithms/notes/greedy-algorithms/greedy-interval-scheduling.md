# Greedy Interval Scheduling

You have a conference room and a list of event requests, each with a start and end time, which makes up the activity interval. Some reservations conflict with each other.

We want to choose a subset of requests that maximizes the number of events that can take place in the conference room without having any of them overlap.

We could choose our greedy criterion to be meeting duration--schedule meetings first that have the shortest duration, eliminate those that conflict, then repeat.

However, this is not optimal because we could cause multiple meetings to conflict with a small meeting and not get the maximum possible number of events.

Instead, let's be "greedy" on the earliest meeting finish time.

Sort events by meeting end time, schedule the first one, and then exclude meetings that overlap with it; repeat this process continuing in ascending order. This gives us the optimal solution!