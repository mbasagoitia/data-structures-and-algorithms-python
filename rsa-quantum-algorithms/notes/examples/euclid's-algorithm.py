def euclids_algorithm(m, n):
    if m < 0: 
        m = -m  # make them positive
    if n < 0: 
        n = -n 
    if m < n:
        (m, n) = (n, m) 
    assert m >= n and m >= 1 and n >= 0
    if n == 0:
        return m if m != 0 else None 
    
    print(f'GCD({m}, {n})')
    
    while n > 0:
        (m, n) = (n, m % n) # the new value of m = n, and new value n = m % n
        print(f'= GCD({m}, {n})')

    assert n == 0
    print(f'= {m}')
    return m

def extended_euclid(m, n):
    assert m >= 1 and n >= 0 and m >= n
    m0, n0 = m, n # let's rememver the initial values
    (s, t) = (1, 0)# m = s * m0 + t * n0
    (s_hat, t_hat) = (0, 1) # n = s_hat * m0 + t_hat * n0
    while n > 0:
        assert m == s * m0 + t * n0
        assert n == s_hat * m0 + t_hat * n0
        q = m // n # compute the integer quotient 
        r = m % n # the reminder 
        # m = q * n + r, or alternatively, r = m - q * n = (s-q*s_hat) * m_0 + (t - q * t_hat)* n_0  
        a, b = (s - q*s_hat, t - q * t_hat)
        (m, n, s, t, s_hat, t_hat) = (n, r, s_hat, t_hat, a, b)
        print(f'GCD({m0}, {n0}) = GCD({m}, {n})')
        print(f'\t {m} = {s}*{m0} + {t} * {n0}')
        print(f'\t {n} = {s_hat}*{m0} + {t_hat} * {n0}')
    return m, s, t
        