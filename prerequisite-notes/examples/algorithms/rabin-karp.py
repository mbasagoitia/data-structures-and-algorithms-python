# This is an example implementation of the Rabin-Karp algorithm for string matching

def rabin_karp(text, pattern):
    d = 256  # number of characters in the input alphabet
    q = 101  # a prime number used for hashing
    m = len(pattern)
    n = len(text)
    h = 1
    p = 0  # hash value for pattern
    t = 0  # hash value for current window of text

    # The value of h would be "pow(d, m-1) % q"
    for i in range(m - 1):
        h = (h * d) % q

    # Calculate the hash value of pattern and first window of text
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        # Check the hash values of current window of text and pattern
        # If the hash values match then only check for characters one by one
        if p == t:
            # Check for characters one by one
            for j in range(m):
                if text[i + j] != pattern[j]:
                    break
            else:
                # if p == t and pattern[0...m-1] == text[i, i+1, ...i+m-1]
                print("Pattern found at index", i)

        # Calculate hash value for next window of text: Remove leading digit, add trailing digit
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + 1])) % q
            # We might get negative value of t, converting it to positive
            if t < 0:
                t = t + q

# Without comments

def rabin_karp(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    h = 1
    p = 0
    t = 0

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            for j in range(m):
                if text[i + j] != pattern[j]:
                    break
            else:
                print("Pattern found at index", i)

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + 1])) % q
            if t < 0:
                t = t + q

