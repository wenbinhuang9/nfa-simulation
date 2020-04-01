# nfa-simulation
Simulate the NFA 

# nfa definition
Define the nfa through file description.

- start denotes on the nfa start state
- accept denotes on the nfa accept state
- the rest of lines are transitions

The definition of nfa as follows is (0|1)*101 
```
start q1
accept q5
q1 0 q1
q1 1 q1
q1 1 q3
q3 0 q4
q4 1 q5
```

# how to use

```
from simulation import getNFAStream, simulate

getNFAStream("./nfa")
simulate(nfa, "101")
```
