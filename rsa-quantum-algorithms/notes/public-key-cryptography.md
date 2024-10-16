# Introduction to Public Key Cryptography

## Secrecy

We will introduce two kinds of cryptography: private-key and public-key

- Private-key:

With a message and a passcode (private key), a message is encrypted and sent, and requires the same passcode to be decrypted by the receiver

- Public-key:

Everyone has two passcodes: a public key and a private (secret) key. Everyone's (unique) public key is publicly available, whereas the private key is not.

A message encrypted using the public key can only be decrypted using the secret key; likewise, a message encrypted by the secret key can only be decrypted by the public key.

The sender encrypts a message with the recipient's public key, which is publicly available, and can only be decrypted by the recipient's private key.

## Authentication

How do we know the identity of the sender if our public keys are available to anyone?

Sender, along with the encrypted message, sends a signature encrypted with their private key. Therefore, the recipient can decrypt the message with the recipient's private key along with the signature, with the sender's public key.

The benefit of public-key cryptography is that it significantly reduces the number of keys needed for communication (2n) vs private-key cryptography.