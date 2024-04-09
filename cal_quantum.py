import numpy as np
from scipy.stats import hmean

def median_burst(burst_time_array: np.ndarray):
    return np.median(burst_time_array)
def average_burst(burst_time_array: np.ndarray):
    return np.mean(burst_time_array)
def average_max_burst(burst_time_array: np.ndarray):
    return (np.mean(burst_time_array)+np.max(burst_time_array))/2
def sqrt_median_HB_burst(burst_tim_array: np.ndarray):
    return np.sqrt(np.median(burst_tim_array)*np.max(burst_tim_array))
def average_median_burst(burst_time_array: np.ndarray):
    return (np.mean(burst_time_array)+np.median(burst_time_array))/2
def sqrt_average_median_burst(burst_time_array: np.ndarray):
    return np.sqrt(np.mean(burst_time_array)*np.median(burst_time_array))
def average_median_max(burst_time_array: np.ndarray):
    return (np.median(burst_time_array)+np.max(burst_time_array))/2
def sqrt_median_max(burst_time_array: np.ndarray):
    return np.sqrt(np.median(burst_time_array)*np.max(burst_time_array))
def min_max_dispersion(burst_time_array: np.ndarray):
    return np.max(burst_time_array)-np.min(burst_time_array)
def harmonic_mean(burst_time_array: np.ndarray):
    return hmean(burst_time_array)
def double_median(bust_time_array: np.ndarray):
    return np.median(bust_time_array)*2