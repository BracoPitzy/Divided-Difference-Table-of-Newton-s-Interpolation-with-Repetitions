import numpy as np
import math

n=6
x=[1,2,2,3.5,3.5,3.5]
y=[0.5,2.5,-0.1,0.3,1,-0.5]

def DividedDiffWithRepetitions(x, y):
    z = [x.count(i) for i in sorted(list(set(x)))]
    xx = [0] * n

    for i in range(1, n):
        xx[i] = xx[i - 1] + (x[i] > x[i - 1])

    coeff = np.zeros((n, n))
    for i in range(n):
        coeff[i][0] = y[sum(z[:xx[i]])]

    for j in range(1, n):
        for i in range(j, n):
            if x[i] != x[i - j]:
                coeff[i][j] = (coeff[i][j - 1] - coeff[i - 1][j - 1]) / (x[i] - x[i - j])
            else:
                coeff[i][j] = y[sum(z[:xx[i]]) + j] / math.factorial(j)
    return coeff

print(DividedDiffWithRepetitions(x, y))

# test
# n=5
# x=[0.4,0.55,0.65,0.80,0.90]
# y=[0.41075,0.57815,0.69675,0.88811,1.02652]

# n=6
# x=[0,0.4,0.8,1.2,1.6,2.0]
# y=[1,1.932,1.6755,0.5575,0.0038,0.7206]