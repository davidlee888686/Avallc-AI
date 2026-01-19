"""Cloud synchronization utilities.

Provides a function to send telemetry or configuration data to a remote
server. Errors are silently ignored to avoid interrupting the application.
"""

import json
import requests  # type: ignore


def sync(data: dict) -> None:
    """Send a JSON payload to a remote server.

    Replace the URL with your actual API endpoint.
    """
    url = "https://yourserver/api/sync"
    try:
        requests.post(url, json=data, timeout=5)
    except requests.exceptions.RequestException:
        # ignore network errors
        pass
