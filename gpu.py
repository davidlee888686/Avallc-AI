"""GPU detection utility.

This module provides a function to check whether a CUDA-capable
GPU is available. If PyTorch is installed, it queries
`torch.cuda.is_available()`. Otherwise, it returns False.
"""



def detect_gpu() -> bool:
    """Return True if a CUDA-capable GPU is available.

    The function attempts to import torch and query its CUDA status.
    If torch is not available or any exception occurs, it returns False.
    """
    try:
        import torch  # type: ignore
        return torch.cuda.is_available()
    except Exception:
        return False
