"""Centralised configuration utilities for Avallc AI.

This module provides helper functions to load configuration values
from either environment variables or a local `.env` file in the
project root. Keeping configuration in one place makes it easier to
manage secrets (like license and encryption keys) without scattering
`os.environ.get` calls throughout the codebase.

The `.env` file format supported here is a very simple key=value
syntax with optional comments starting with `#`. Lines that cannot
be parsed are ignored. Values defined in the environment take
precedence over those in the `.env` file.

Example `.env` file::

    # Example configuration for Avallc AI
    AVA_LICENSE_KEY=abcdef1234567890
    AVA_ENCRYPTION_KEY=some-secret-key

Functions
---------
get_license_key() -> str | None
    Return the license key string, if provided.

get_encryption_key() -> bytes
    Return the encryption key bytes for decrypting model files.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Optional, Dict

_DOTENV_CACHE: Optional[Dict[str, str]] = None



def _load_dotenv() -> Dict[str, str]:
    """Load configuration from a local .env file.

    Parses key=value pairs from a file named `.env` located in the
    directory containing this module. Environment variables always
    override values loaded from the file.

    Returns a dictionary mapping keys to values. The result is cached
    to avoid repeated file I/O on subsequent calls.
    """
    global _DOTENV_CACHE
    if _DOTENV_CACHE is not None:
        return _DOTENV_CACHE

    result: Dict[str, str] = {}
    dotenv_path = Path(__file__).resolve().parent / ".env"
    if dotenv_path.exists():
        try:
            for line in dotenv_path.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    key, value = line.split("=", 1)
                    result[key.strip()] = value.strip()
        except Exception:
            # Ignore parsing errors and fall back to empty config
            result = {}

    _DOTENV_CACHE = result
    return result



def get_license_key() -> Optional[str]:
    """Return the license key to use for validating the application.

    Checks the `AVA_LICENSE_KEY` environment variable first. If not
    present, attempts to read the key from a `.env` file. Returns
    ``None`` if no key is found.
    """
    env_key = os.environ.get("AVA_LICENSE_KEY")
    if env_key:
        return env_key
    return _load_dotenv().get("AVA_LICENSE_KEY")



def get_encryption_key() -> bytes:
    """Return the encryption key for decrypting model files.

    Checks the `AVA_ENCRYPTION_KEY` environment variable first. If not
    present, attempts to read the key from a `.env` file. If still
    undefined, falls back to a static placeholder. In a production
    environment you should replace this placeholder with a secure
    generated key.

    Returns
    -------
    bytes
        The encryption key encoded as UTF-8 bytes.
    """
    key = os.environ.get("AVA_ENCRYPTION_KEY") or _load_dotenv().get(
        "AVA_ENCRYPTION_KEY"
    )
    if key:
        return key.encode()
    # WARNING: using a static key is insecure. Generate your own key
    # with `cryptography.fernet.Fernet.generate_key()` and set it in
    # the environment or .env file.
    return b"YOUR_STATIC_KEY"
