# RSA Cryptography Scheme

Public-key cryptosystem that forms the basis of modern internet communication; based on difficulty of factoring semi-prime numbers

Alphanumeric messages are converted to numbers using their ASCII representations (that can be reconstructed in the same way)

## Basic Idea

We calculate some number n which is the product of two very large (> 2^1000) prime numbers, p and q. With this, we will construct our private and public keys.

Public key: (e, n) where e is some number that is relatively prime with n, and n is p * q. Remember two numbers are relatively prime if their GCD is 1. 

Private key: (d, n) where d is chosen so that (M^e % n) ^ d % n = M, or alternatively, (M hat ^ d) % n = M

M and n must be relatively prime

M ^ e*d % n = M

## Encryption/Decryption in RSA

Encryption:

M^e % n = M hat (encrypted message), where M is the number representation of the message (as stated above using ASCII)

M (message value) must also be relatively prime with n

Decryption: M hat ^ d % n = M (original message)