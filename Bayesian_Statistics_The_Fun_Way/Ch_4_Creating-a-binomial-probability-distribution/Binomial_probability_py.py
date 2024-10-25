# Binomial probability distribution from scratch
# Drawing a card with replacement a 100 times and we want it at least once
import math
import numpy as np

p = 0.0072
k = 1
n = 100
cumulative_prob = 0

for k in range(1,n):
    prob = math.comb(n, k)*p**k*(1-p)**(n-k)
    cumulative_prob += prob

cumulative_prob

# Another way, would be to just say:
# whats the probability of NOT getting that one special card
prob = math.comb(n, 0)*p**0*(1-p)**(n-0)
print(f'Probability of getting that one card is then: {1-prob}')

round((1-prob), 5) == round(cumulative_prob,5)


# 4
p = 0.2
n = 7
cumulative_prob_7_interviews = 0
probs = []

for k in range(2,n):
    prob = math.comb(n, k)*p**k*(1-p)**(n-k)
    probs.append(prob)
    cumulative_prob_7_interviews += prob



# 5
n = 25
p = 0.1
cumulative_prob_25_interviews = 0
probs = []

for k in range(2,n):
    prob = math.comb(n, k)*p**k*(1-p)**(n-k)
    probs.append(prob)
    cumulative_prob_25_interviews += prob

cumulative_prob_25_interviews/cumulative_prob_7_interviews

for i in range(2, 7):
    print(i)