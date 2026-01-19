"""Windows service logic for Avallc AI.

This module defines a simple service loop that repeatedly calls the
application entry point. You can use this with a service wrapper such as
NSSM to run your application as a Windows service.
"""

import time
from main import run_app


def service_loop(interval: float = 5.0) -> None:

    """Run the application in a loop with a pause between iterations."""
    while True:
        run_app()
        time.sleep(interval)
