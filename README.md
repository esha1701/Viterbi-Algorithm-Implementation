# Viterbi-Algorithm-Implementation

A Markov process is a process wherein the current (nth) state of the system only depends on the previous (n-1th) state of the system. They are ‘memoryless’ processes.

Let’s say we have a Markovian process X and we want to model its behaviour. X, however, can not be directly observed. X has “hidden states”, which means we can not see what state X is at. There is, however, an observable process Y whose behaviour depends on X. Hidden Markov Models are a statistical tool which help infer the most probable state of X by observing the states of Y.  

Decoding Problems are one of the three basic problems in Hidden Markov Models. It is used to find a sequence of hidden states (states of X) given a sequence of observable states (states of Y). This code is an implementation of the Viterbi Algorithm which is a dynamic programming algorithm used for decoding problems.


I considered exercising every day a Markovian process, wherein the chances of exercising today depend on if you exercised yesterday or were sedentary (if you are like me at least!). The observed states are change in weight. You could either gain weight, lose weight or observe no change. I calculated the probabilities based on a 10 day sample of my recorded data. 
