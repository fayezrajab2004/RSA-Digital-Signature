# RSA Digital Signature

A simple Python program that demonstrates how RSA digital signatures work.

## Features
- Generate RSA public and private keys.
- Sign a message using the private key.
- Verify the signature using the public key.
- Detect changes to the original message.

## Requirements
- Python 3.10 or later
- cryptography library

## Installation

```bash
py -m pip install cryptography
```

## Run

```bash
py rsa_signature.py
```

## Expected Results

- Original message: Signature is VALID.
- Modified message: Signature is INVALID.

## Course
Software Security – Chapter 2: Cryptographic Tools