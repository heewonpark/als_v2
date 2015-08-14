import numpy as np

mat = []
for i in range(5):
    rnd = []
    while len(rnd)<17:
        rnd.append(np.random.randint(35))
        rnd = list(set(rnd))
    mat.append(rnd)
print mat
