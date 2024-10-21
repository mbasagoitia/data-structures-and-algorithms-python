# RSA Cryptography Scheme

Public-key cryptosystem that forms the basis of modern internet communication; based on difficulty of factoring semi-prime numbers

Alphanumeric messages are converted to numbers using their ASCII representations (that can be reconstructed in the same way)

## Basic Idea

We calculate some number n which is the product of two very large (> 2^1000) prime numbers, p and q. With this, we will construct our private and public keys.

Public key: (e, n) where e is some random number that is relatively prime with n, and n is p * q. Remember two numbers are relatively prime if their GCD is 1. 

Private key: (d, n) where d is chosen so that (M^e % n) ^ d % n = M, or alternatively, (M hat ^ d) % n = M

The public and private key must work for every message M

M and n must be relatively prime

M ^ e*d % n = M

## Encryption/Decryption in RSA

Encryption:

M^e % n = M hat (encrypted message), where M is the number representation of the message (as stated above using ASCII)

M (message value) must also be relatively prime with n

Decryption: M hat ^ d % n = M (original message)

We have to choose d such that M^e*d % n = M (requirement) <- this essentially says that encryption followed by decryption gives you back the original message for every message M. Finding d is the main question.

## Euler Totient Theorem

Suppose we have a number n. A function fi(n) known as the totient function counts the number of relatively prime numbers < n to n. If you take any M relatively prime with n, then **M^fi(n) %  n = 1**

f(n) = count of numbers a, such that a is relatively prime to n

Ex. n = 55

The numbers relatively prime with 55 are as follows:

values of a = {1, 2, 3, 4, 6, 7, 8, 9, 12, 13, 14, 16, 17, 18, 19, ...} <- count is 40, so f(n) = 40

fi(55) = 40

M must be relatively prime with n, so say M = 7.

Sure enough, 7^40 % 55 = 1

Furthermore, remember n = p * q.

**fi(n) = fi(p * q) = (p - 1) * (q - 1)**

Make sure that when you choose e, it is relatively prime with both n and fi(n). In other words, GCD(e, fi(n)) = 1

By Bezout's theorem, GCD(e, fi(n)) = 1, so e * _ + fi(n) * _ = 1 where _ are Bezout coefficients. Let's say that the first _ is d and the second is v. We can manipulate d to be positive and v to be negative so that it satisfies this equality.

We will end up with **e * d = 1 + fi(n) * v** (v doesn't really matter), and d is the decryption key.

Choosing d in this way ensures that M ^ e*d % n = M

## Hardness of Factoring Prime Numbers

It turns out that given a very large prime mumber n, finding its factors p and q (and by extension, d) is a hard problem (exponential). This is what RSA relies on.
