import numpy as np


def median_burst(burst_time_array: np.ndarray):
    return np.median(burst_time_array)
def average_burst(burst_time_array: np.ndarray):
    return np.mean(burst_time_array)
def average_max_burst(burst_time_array: np.ndarray):
    return (np.mean(burst_time_array)+np.max(burst_time_array))/2
def sqrt_median_HB_burst(burst_tim_array: np.ndarray):
    return np.sqrt(np.mean(burst_tim_array)*np.max(burst_tim_array))
def average_median_burst(burst_time_array: np.ndarray):
    return (np.mean(burst_time_array)+np.median(burst_time_array))/2
def sqrt_average_median_burst(burst_time_array: np.ndarray):
    return np.sqrt(np.mean(burst_time_array)*np.median(burst_time_array))
def average_median_max(burst_time_array: np.ndarray):
    return (np.median(burst_time_array)+np.max(burst_time_array))/2
def sqrt_median_max(burst_time_array: np.ndarray):
    return np.sqrt(np.median(burst_time_array)*np.max(burst_time_array))