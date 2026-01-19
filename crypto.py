"""Simple encryption/decryption utilities.

This module provides an example of how you might decrypt an encrypted
model file using a symmetric key. Replace `KEY` with your own secure key.
"""

from cryptography.fernet import Fernet  # type: ignore

try:
    # When used as part of the avallc_ai_project package
    from .config import get_encryption_key  # type: ignore
except ImportError:
    # Fallback if the module is executed as a script without package context
    from config import get_encryption_key  # type: ignore

# Retrieve the key once at import time. In a long‑running application
# you might want to refresh this periodically if the environment or
# .env file can change during runtime.
KEY: bytes = get_encryption_key()


def decrypt_model(path: str) -> bytes:
    """Decrypt and return the contents of an encrypted model file."""
    with open(path, "rb") as f:
        data = f.read()
    return Fernet(KEY).decrypt(data)
