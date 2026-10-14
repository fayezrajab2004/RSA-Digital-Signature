
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

# Generate RSA private and public keys
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

public_key = private_key.public_key()

print("RSA keys generated successfully.")


# Create a message
message = b"Hello Bob, this message is from Alice."

# Sign the message using the private key
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("Original message:", message.decode())
print("Digital signature created successfully.")



# Verify the digital signature using the public key
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    print("Signature is VALID.")

except InvalidSignature:
    print("Signature is INVALID.")

    

    
# Modify the original message
modified_message = b"Hello Bob, this message is from Oscar."

print("Modified message:", modified_message.decode())

# Verify the modified message using the original signature
try:
    public_key.verify(
        signature,
        modified_message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    print("Modified message signature is VALID.")

except InvalidSignature:
    print("Modified message signature is INVALID.")


