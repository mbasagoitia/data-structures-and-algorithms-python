# Calculating the DFT of a Sequence

import cmath
import math

def nth_root_of_unity(N, k):
    return cmath.exp(-2j * math.pi * k / N)

seq = [1, 2, 3, 4]

def calculate_dft(seq):
    N = len(seq)
    dft = [0] * N

    for k in range(N):
        value = 0
        for n in range(N):
            value += seq[n] * nth_root_of_unity(N, k * n)
        dft[k] = value
    
    return dft

print(calculate_dft(seq))