def karatsuba(x, y):
    """Multiply two binary numbers using Karatsuba's algorithm."""
    # Ensure x and y are strings of the same length
    n = max(len(x), len(y))
    if n % 2 != 0:
        n += 1
    x = x.zfill(n)
    y = y.zfill(n)
    
    # Base case
    if len(x) == 1:
        return str(int(x) * int(y))
    
    # Split the binary numbers
    m = len(x) // 2
    x1, x0 = x[:m], x[m:]
    y1, y0 = y[:m], y[m:]
    
    # Recursively calculate three products
    z2 = karatsuba(x1, y1)
    z0 = karatsuba(x0, y0)
    z1 = karatsuba(binary_add(x1, x0), binary_add(y1, y0))
    z1 = binary_subtract(z1, binary_add(z2, z0))
    
    # Combine the results
    result = binary_add(binary_shift(z2, 2 * m), binary_add(binary_shift(z1, m), z0))
    return result

def binary_add(a, b):
    """Add two binary numbers represented as strings."""
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    
    result = []
    carry = 0
    for i in range(max_len - 1, -1, -1):
        total = int(a[i]) + int(b[i]) + carry
        result.append(str(total % 2))
        carry = total // 2
    
    if carry:
        result.append('1')
    
    return ''.join(result[::-1])

def binary_subtract(a, b):
    """Subtract binary number b from binary number a."""
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    
    result = []
    borrow = 0
    for i in range(max_len - 1, -1, -1):
        diff = int(a[i]) - int(b[i]) - borrow
        if diff < 0:
            diff += 2
            borrow = 1
        else:
            borrow = 0
        result.append(str(diff))
    
    return ''.join(result[::-1]).lstrip('0') or '0'

def binary_shift(a, n):
    """Shift binary number a to the left by n bits."""
    return a + '0' * n

