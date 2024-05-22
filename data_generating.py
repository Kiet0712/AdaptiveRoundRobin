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
COUNT = {

}
METHODMAPPING = {

}
a = 0
for key in METHOD_ZOO:
  METHODMAPPING[key] = a
  a+=1
cache_process = None
cache_burst_time_array = None
cache_arrival_time_array = None
N1 = 19000
N2 = 1000

DATA_TRAIN_N1 = []
DATA_TRAIN_N2 = []

for i in range(N1):
    sample ={}
    #bit_masks = []
    while 1:
            bit_mask = [random.uniform(0,1) for _ in range(5)]
            if np.sum(bit_mask) == 0:
                 continue
            else:
                 break
    processes,burst_time_array,arrival_time_array = sampling_process(
    30,100,0,5,random.randint(3,20)
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
    if min_key not in COUNT:
      COUNT[min_key]=1
    else:
      COUNT[min_key]+=1
    sample.update({'process' :process})
    sample.update({'label' : min_key})
    sample.update({'binary mask': bit_mask})

    DATA_TRAIN_N1.append(sample)
import matplotlib.pyplot as plt
def plot(count,dataset):
    fig, ax1 = plt.subplots(1, 1,figsize=(12,6))
    method = [key for key in count]
    count_method = [count[key] for key in count]
    y_pos = np.arange(len(method))
    ax1.barh(y_pos,count_method,align='center')
    ax1.set_yticks(y_pos, labels=method)
    ax1.invert_yaxis()
    ax1.set_xlabel('count')
    ax1.set_ylabel('method')
    ax1.set_title(dataset + ' bar chart')
    #ax2.pie(count_method,labels=method, autopct="%1.1f%%")
    #ax2.set_title(dataset + ' pie chart')
    plt.show()
print(COUNT)
plot(COUNT,'train dataset')
for i in range(N2):
    sample ={}
    #bit_masks = []
    while 1:
            bit_mask = [random.uniform(0,1) for _ in range(5)]
            if np.sum(bit_mask) == 0:
                 continue
            else:
                 break
    processes,burst_time_array,arrival_time_array = sampling_process(
    30,100,0,5,random.randint(3,20)
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
import pickle
with open("train_dataset", "wb") as fp:
     pickle.dump(DATA_TRAIN_N1, fp)
with open("val_dataset", "wb") as fp:
     pickle.dump(DATA_TRAIN_N2, fp)