"""Simple encryption/decryption utilities.

This module provides an example of how you might decrypt an encrypted
model file using a symmetric key. Replace `KEY` with your own secure key.
"""

fromfrom cryptography.fernet import Fernet  # type: ignore
import os

# Determine the encryption key for decrypting model files.
# In production, the key should be provided via an environment variable
# so that the code does not contain secrets. If the environment variable
# `AVA_ENCRYPTION_KEY` is set, it will be used. Otherwise, a static
# placeholder key is used as a fallback. Replace this placeholder with
# your own generated key or configure the environment variable.

_env_key = os.environ.get("AVA_ENCRYPTION_KEY")
if _env_key:
    KEY: bytes = _env_key.encode()
else:
    # WARNING: using a static key is insecure. Generate your own key
    # with `Fernet.generate_key()` and provide it via the environment.
    KEY: bytes = b"YOUR_STATIC_KEY"

def decrypt_model(path: str) -> bytes:
    """Decrypt and return the contents of an encrypted model file."""
    with open(path, "rb") as f:
        data = f.read()
    return Fernet(KEY).decrypt(data)
