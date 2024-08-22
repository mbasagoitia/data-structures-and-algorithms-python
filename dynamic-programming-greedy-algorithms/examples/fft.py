# Fast Fourier Transform Divide and Conquer

# cmath allows you to use complex numbers
import cmath

# Calculate nth roots of unity
import math
def get_roots_of_unity(n):
    assert n >= 2
    angles = [2.0 * math.pi * k/n for k in range(n)]
    lst = [math.cos(ang) + math.sin(ang) * 1j for ang in angles]
    return lst

# Calculate the FFT
def fft(seq):
    # Base case
    if len(seq) == 1:
        return seq
    else:
        n = len(seq)
        # Sequence length must be even/power of two
        assert n % 2 == 0
        seq_even = [seq[2*j] for j in range(n // 2)]
        seq_odd = [seq[2*j + 1] for j in range(n // 2)]
        s1 = fft(seq_even)
        s2 = fft(seq_odd)
        fft_ret = [0]*n
        w = 1.0
        wn = (math.cos(2.0 * math.pi/n) + math.sin(2.0 * math.pi/n) * 1j)
        for k in range(n // 2):
            fft_ret[k] = (s1[k] + w * s2[k])
            fft_ret[k + n // 2] = (s1[k] - w * s2[k])
            w = w*n
        return fft_ret
    
# Calculate the inverse FFT
def inverse_fft(seq):
    # Base case
    if len(seq) == 1:
        return seq
    else:
        n = len(seq)
        assert n % 2 == 0
        seq_even = [seq[2*j] for j in range(n // 2)]
        seq_odd = [seq[2*j + 1] for j in range(n // 2)]
        s1 = fft(seq_even)
        s2 = fft(seq_odd)
        fft_ret = [0]*n
        w = 1.0
        wn = (math.cos(2.0 * math.pi/n) + math.sin(2.0 * math.pi/n) * 1j)
        for k in range(n // 2):
            fft_ret[k] = 0.5 * (s1[k] + w * s2[k])
            fft_ret[k + n // 2] = 0.5 * (s1[k] - w * s2[k])
            w = w*n
        return fft_ret
