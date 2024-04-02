import random
import numpy as np


def sampling_process(
        mean_burst_time: float,
        std_burst_time: float,
        mean_arrival_time: float,
        std_arrival_time: float,
        num_process: int
    ) -> list[tuple]:
    burst_time_array = np.int32(np.random.normal(loc=mean_burst_time,scale=std_burst_time,size=num_process))
    arrival_time_array = np.int32(np.random.normal(loc=mean_arrival_time,scale=std_arrival_time,size=num_process))
    result_sampling = []
    for i in range(num_process):
        result_sampling.append((i,arrival_time_array[i],burst_time_array[i]))
    return result_sampling,burst_time_array,arrival_time_array