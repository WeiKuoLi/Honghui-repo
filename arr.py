import numpy as np

def integrate(arr: np.ndarray, dx: float) -> float:
    return np.sum(arr) * dx


