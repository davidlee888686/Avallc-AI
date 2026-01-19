"""Simple encryption/decryption utilities.

This module provides an example of how you might decrypt an encrypted
model file using a symmetric key. Replace `KEY` with your own secure key.
"""

from cryptography.fernet import Fernet  # type: ignore

# Replace with your real key (generated with `Fernet.generate_key()`)
KEY: bytes = b"YOUR_STATIC_KEY"


def decrypt_model(path: str) -> bytes:
    """Decrypt and return the contents of an encrypted model file."""
    with open(path, "rb") as f:
        data = f.read()
    return Fernet(KEY).decrypt(data)
