"""
Generate points from K different realizations

Source:
DISCRETE-EVENT SIMULATION: A FIRST COURSE
L.Leemis & S.Park

Algorithm 9.3.1
"""

import numpy as np
from scipy import stats
from sparklines import sparklines

np.random.seed(42)

data = np.array([
    [1, 2, 4, 4, 6, 4, 3, 1, 1],  # seed=1
    [1, 3, 2, 5, 6, 5, 6, 2, 0],  # seed=2
    [0, 3, 1, 5, 7, 5, 4, 3, 0],  # seed=3
])
a = np.arange(0, 5, 0.5)
n = data.sum(axis=0)

m = 9
k = 3

dist = stats.expon()

lmb_max = sum(n / k)
E = dist.rvs()
T = []
i = 1
j = 0

lmb = n[i - 1] / k

while E <= lmb_max:
    while E > lmb:
        i += 1
        lmb += n[i - 1] / k

    T.append(a[i] - (lmb - E) * k * (a[i] - a[i - 1]) / n[i - 1])
    E += dist.rvs()
T.pop()

events = [len([x for x in T if l < x <= r]) for l, r in zip(a, a[1:])]
for i, x in enumerate(data):
    print(f'or{i}', sparklines(x)[0], x, sum(x))
print('gen', sparklines(events)[0], np.array(events), len(T))
print(T)
