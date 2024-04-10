from sampling import sampling_process
from standard_round_robin import constant_round_robin
from cal_quantum import *
import random
import time
import json

random.seed(time.time())

METHOD_ZOO = {
    'median':(median_burst,constant_round_robin),
    'average':(average_burst,constant_round_robin),
    'average_max':(average_max_burst,constant_round_robin),
    'sqrt\nmedian_HB':(sqrt_median_HB_burst,constant_round_robin),
    'average\nmedian':(average_median_burst,constant_round_robin),
    'sqrt_average\nmedian':(sqrt_average_median_burst,constant_round_robin),
    'average\nmedian_max':(average_median_max,constant_round_robin),
    'sqrt\nmedian_max':(sqrt_median_max,constant_round_robin),
    'minmax\ndispersion':(min_max_dispersion,constant_round_robin),
    'harmonic\nmean': (harmonic_mean,constant_round_robin),
    'double\nmedian':(double_median,constant_round_robin)
}

cache_process = None
cache_burst_time_array = None
cache_arrival_time_array = None
N1 = 8000
N2 = 1000
N3 = 1000

DATA_TRAIN_N1 = []
DATA_TRAIN_N2 = []
DATA_TRAIN_N3 = []

for i in range(N1):
    sample ={}
    bit_masks = []
    while 1:
            bit_mask = [random.choice([0,1]) for _ in range(5)]
            if np.sum(bit_mask) == 0:
                 continue
            else:
                 break
    processes,burst_time_array,arrival_time_array = sampling_process(
    100,40,20,3,random.randint(3,20)
    )
    if i!=0 and random.uniform(0,1)>0.5:
         processes,burst_time_array,arrival_time_array = cache_process,cache_burst_time_array,cache_arrival_time_array
    #proccess : list of tuple of burst time and arrival time
    cache_process,cache_burst_time_array,cache_arrival_time_array = processes,burst_time_array,arrival_time_array
    process = list(zip(burst_time_array,arrival_time_array))
    data = {}
    for method in METHOD_ZOO:

        cal_quantum,round_robin = METHOD_ZOO[method]
        quantum_time = np.int32(cal_quantum(burst_time_array))
        #print(process,quantum_time,method)
        avg_turnaround_time, avg_waiting_time, avg_response_time, context_switches, var_response = round_robin(processes, quantum_time)
        metrics = [avg_turnaround_time,avg_waiting_time,avg_response_time,context_switches,var_response]
        value = np.sum(np.array(metrics)*np.array(bit_mask))/np.sum(bit_mask)
        data.update({method : value})




    min_key = min(data, key=data.get)
    sample.update({'process' :process})
    sample.update({'label' : min_key})
    sample.update({'binary mask': bit_mask})

    DATA_TRAIN_N1.append(sample)

for i in range(N2):
    sample ={}
    bit_masks = []
    while 1:
            bit_mask = [random.choice([0,1]) for _ in range(5)]
            if np.sum(bit_mask) == 0:
                 continue
            else:
                 break
    processes,burst_time_array,arrival_time_array = sampling_process(
    100,40,20,3,random.randint(3,20)
    )
    if i!=0 and random.uniform(0,1)>0.5:
         processes,burst_time_array,arrival_time_array = cache_process,cache_burst_time_array,cache_arrival_time_array
    #proccess : list of tuple of burst time and arrival time
    cache_process,cache_burst_time_array,cache_arrival_time_array = processes,burst_time_array,arrival_time_array
    process = list(zip(burst_time_array,arrival_time_array))
    data = {}
    for method in METHOD_ZOO:

        cal_quantum,round_robin = METHOD_ZOO[method]
        quantum_time = np.int32(cal_quantum(burst_time_array))
        #print(process,quantum_time,method)
        avg_turnaround_time, avg_waiting_time, avg_response_time, context_switches, var_response = round_robin(processes, quantum_time)
        metrics = [avg_turnaround_time,avg_waiting_time,avg_response_time,context_switches,var_response]
        value = np.sum(np.array(metrics)*np.array(bit_mask))/np.sum(bit_mask)
        data.update({method : value})




    min_key = min(data, key=data.get)
    sample.update({'process' :process})
    sample.update({'label' : min_key})
    sample.update({'binary mask': bit_mask})

    DATA_TRAIN_N2.append(sample)


for i in range(N3):
    sample ={}
    bit_masks = []
    while 1:
            bit_mask = [random.choice([0,1]) for _ in range(5)]
            if np.sum(bit_mask) == 0:
                 continue
            else:
                 break
    processes,burst_time_array,arrival_time_array = sampling_process(
    100,40,20,3,random.randint(3,20)
    )
    if i!=0 and random.uniform(0,1)>0.5:
         processes,burst_time_array,arrival_time_array = cache_process,cache_burst_time_array,cache_arrival_time_array
    #proccess : list of tuple of burst time and arrival time
    cache_process,cache_burst_time_array,cache_arrival_time_array = processes,burst_time_array,arrival_time_array
    process = list(zip(burst_time_array,arrival_time_array))
    data = {}
    for method in METHOD_ZOO:

        cal_quantum,round_robin = METHOD_ZOO[method]
        quantum_time = np.int32(cal_quantum(burst_time_array))
        #print(process,quantum_time,method)
        avg_turnaround_time, avg_waiting_time, avg_response_time, context_switches, var_response = round_robin(processes, quantum_time)
        metrics = [avg_turnaround_time,avg_waiting_time,avg_response_time,context_switches,var_response]
        value = np.sum(np.array(metrics)*np.array(bit_mask))/np.sum(bit_mask)
        data.update({method : value})




    min_key = min(data, key=data.get)
    sample.update({'process' :process})
    sample.update({'label' : min_key})
    sample.update({'binary mask': bit_mask})

    DATA_TRAIN_N3.append(sample)

import pickle
file_path = "DATA_TRAIN.pkl"

# Save the list to a file using pickle
with open("DATA_TRAIN_N1.pkl", "wb") as f:
    pickle.dump(DATA_TRAIN_N1, f)

with open("DATA_TRAIN_N2.pkl", "wb") as f:
    pickle.dump(DATA_TRAIN_N2, f)

with open("DATA_TRAIN_N3.pkl", "wb") as f:
    pickle.dump(DATA_TRAIN_N3, f)


    
