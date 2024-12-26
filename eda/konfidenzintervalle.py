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


def bootstrap_konfidenzintervall(data: np.ndarray, confidence_level: float = 0.95, n_iterations: int = 10000) -> tuple:
    """
    Berechnet das Konfidenzintervall für eine gegebene Stichprobe unter Verwendung von Bootstrapping.

    :param data: Eine numpy-Array, das die Stichprobe enthält.
    :param confidence_level: Das gewünschte Konfidenzniveau (Standardwert ist 0,95 für 95%).
    :param n_iterations: Die Anzahl der Bootstrapping-Wiederholungen (Standardwert ist 10000).
    :return: Ein Tuple, das das Konfidenzintervall enthält (untere Grenze, obere Grenze).
    """
    bootstrap_means = []

    # Bootstrapping-Prozess
    for _ in range(n_iterations):
        sample = np.random.choice(data, size=len(data), replace=True)
        bootstrap_means.append(np.mean(sample))

    ci_lower = np.percentile(bootstrap_means, 2.5)
    ci_upper = np.percentile(bootstrap_means, 97.5)

    return ci_lower, ci_upper