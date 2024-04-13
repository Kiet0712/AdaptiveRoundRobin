import random
import numpy as np
import time

def random_arrival_time_in_range(i,j,mean,std,num_process):
    arrival_time_array = []
    while len(arrival_time_array) < num_process :
        num = np.random.normal(mean,std)
        if i <= num <= j:
            arrival_time_array.append(num)

    
    return arrival_time_array

def sampling_process(
        min_burst_time: int,
        max_burst_time: int,
        min_arrival_time: int,
        max_arrival_time: int,
        num_process: int
    ) -> list[tuple]:
    #burst_time_array = np.int32(np.exp(np.random.normal(loc=mean_burst_time,scale=std_burst_time,size=num_process)))
    burst_time_array = np.random.randint(min_burst_time,max_burst_time,size=num_process)
    #arrival_time_array = np.int32(np.exp(np.random.normal(loc=mean_arrival_time,scale=std_arrival_time,size=num_process)))
    #arrival_time_array = np.int32(random_arrival_time_in_range(0,100,mean_arrival_time,std_arrival_time,num_process))
    arrival_time_array = np.random.randint(min_arrival_time,max_arrival_time,size=num_process)
    result_sampling = []
    for i in range(num_process):
        result_sampling.append((i,arrival_time_array[i],burst_time_array[i]))
    return result_sampling,burst_time_array,arrival_time_array