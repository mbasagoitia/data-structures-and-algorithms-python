# Data Analysis using FFT

Given a signal sampled at many different points a0 ... an-1 at a time interval of delta T (0.001s), take the FFT of the set of points to get [A0 ... An-1]. Each component corresponds to a frequency. A0, the first value, represents the average value of the signal (DC or direct current component). A1 - An-1 correspond to various frequencies.

- If n = 1,000 and delta T = 0.001:
    - The frequency of A1 is 1/1000 * 1/0.001 which = 1 Hz
    - This is given by the formula frequency of Ai = **i/n * 1/delta T**
    - A2 would be 2 Hz (2 oscillations per second)

*Special Property*

A0 = A0

A1 and An-1 are complex conjugates
A2 and An-2 are complex conjugates
An/2 - 1 and An/2 + 1 are complex conjugates

An/2 (middle) stands by itself and is typically a real value

Whenever you take the FFT of a sequence of real numbers, you have this symmetry. So we only need to interpret frequencies up to n/2, and beyond that would be negative frequencies that can be predicted by taking the complex conjugate of the first half of the series.

## Example: Weekly Commodity Prices

- delta T = 1 week
- n = 1024 (weeks), which is about 20 years

We will analyze up to 512 weeks, interpreted as a frequency of 1 every 2 weeks

Each frequency A1 ... An-1 is i/n, or 1/1024, 2/1024, etc.

As you increase the x number of lowest frequencies, the signal becomes more specific to the data (rewatch this lecture)