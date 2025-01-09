import numpy as np
import scipy.stats as stats

def konfidenzintervall(data: np.ndarray, confidence_level: float = 0.95, method: str = 'auto') -> tuple:
    """
    Berechnet das Konfidenzintervall für eine gegebene Stichprobe und Konfidenzniveau.

    :param data: Eine numpy-Array, das die Stichprobe enthält.
    :param confidence_level: Das gewünschte Konfidenzniveau (Standardwert ist 0,95 für 95%).
    :param method: Methode zur Berechnung des Konfidenzintervalls: 'normal', 't', oder 'auto' (Standard).
    :return: Ein Tuple, das das Konfidenzintervall enthält (untere Grenze, obere Grenze).
    """
    mean = np.mean(data)
    std_err = stats.sem(data)
    n = len(data)

    if method == 'normal' or (method == 'auto' and n > 30):
        confidence_interval = stats.norm.interval(confidence_level, loc=mean, scale=std_err)
    elif method == 't' or (method == 'auto' and n <= 30):
        confidence_interval = stats.t.interval(confidence_level, n-1, loc=mean, scale=std_err)
    else:
        raise ValueError("Invalid method specified. Choose 'normal', 't', or 'auto'.")

    return confidence_interval