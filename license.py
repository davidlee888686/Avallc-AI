"""License utilities.

Provides simple functions to generate a device ID and validate a license key
for the Avallc AI application. In a real application, license validation
would involve secure key verification and perhaps a server check.
"""

import uuid
import hashlib


def device_id() -> str:
    """Return a unique device identifier based on the machine's MAC address."""
    return hashlib.sha256(str(uuid.getnode()).encode()).hexdigest()


def validate_license(key: str) -> bool:
    """Validate the provided license key.

    Currently checks if the key equals the computed device ID. Replace
    with proper validation logic in production.
    """
    return key == device_id()
