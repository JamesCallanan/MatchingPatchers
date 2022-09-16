# MatchingPatchers

Algorithm to pairwise match patch cohort members in order to maximise meet ups between members who do not know each other or do not know each other well.

# To Do:

- Build so it works with odd number of Patch members
- Need to update closenesses following pairings, this ensures that in following weeks we don't match the same people
- Build approximate solution method on the off chance more than 18 patchers sign up

## Optimal soln

As this is an NP-Hard problem, an optimal solution is returned by default when the number of members is <= 18.

Time taken to pair 18 people was 270.02 s

Lower bound predicted time to pair 20 people = 19\*270.02 = 5130.4 s = 85.5 mins
In reality, I suspect it is far larger ~ 7 hours maybe

Thus, if 20 patchers were to sign up, we would need an approximate soln.

### Note on time predictions for pairing 20 patchers:

Time taken to pair 12 people was 0.02 s
Prediction for 14 = 0.02\*13 = 0.30 s

Time taken to pair 14 people was 0.34 s
Prediction for 16 = 0.34\*15 = 5.10 s

Time taken to pair 16 people was 5.61 s
Prediction for 18 = 5.61\*17 = 95.30 s

Time taken to pair 18 people was 270.02 s

Predictions are no longer accurate.
I predicted 5.61\*17 = 95.3 s as the number of pairwise combinations should be 17 times more.
However, each combo is also one pair longer. This means other calculations scale. Multiplying by 17 doesn't account for the other calculations scaling.

Thus, this method of predicting the time needed for finding the optimal pairing of n patchers can only be used to calculate a lower bound.

### Sample output for pairing of 18 people

Pairing with min closeness score = [('244', '314'), ('322', '432'), ('322', '432'), ('322', '432'), ('414', '432'), ('322', '413'), ('414', '432'), ('414', '432'), ('231', '311')]
with a closeness score of ... 0.8999999999999999
