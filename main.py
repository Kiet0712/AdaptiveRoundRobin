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
METHODMAPPING = {

}
a = 0
for key in METHOD_ZOO:
  METHODMAPPING[key] = a
  a+=1
cache_process = None
cache_burst_time_array = None
cache_arrival_time_array = None
N1 = 18000
N2 = 1000
N3 = 1000

DATA_TRAIN_N1 = []
DATA_TRAIN_N2 = []
DATA_TRAIN_N3 = []

for i in range(N1):
    sample ={}
    bit_masks = []
    while 1:
            bit_mask = [random.uniform(0,1) for _ in range(5)]
            if np.sum(bit_mask) == 0:
                 continue
            else:
                 break
    processes,burst_time_array,arrival_time_array = sampling_process(
    50,100,0,10,random.randint(3,20)
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
            bit_mask = [random.uniform(0,1) for _ in range(5)]
            if np.sum(bit_mask) == 0:
                 continue
            else:
                 break
    processes,burst_time_array,arrival_time_array = sampling_process(
    50,100,0,10,random.randint(3,20)
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
            bit_mask = [random.uniform(0,1) for _ in range(5)]
            if np.sum(bit_mask) == 0:
                 continue
            else:
                 break
    processes,burst_time_array,arrival_time_array = sampling_process(
    50,100,0,10,random.randint(3,20)
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
NUM_EPOCH = 40
D_MODEL = 8
N_HEAD = 2
DROP_PROB = 0.1
N_ENCODER = 1
N_CLASS = len(METHOD_ZOO)
from model import Model
import torch
import torch.nn as nn
import numpy as np

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')\

model = Model(D_MODEL,N_HEAD,DROP_PROB,N_ENCODER,N_CLASS).to(device)

total_params = sum(p.numel() for p in model.parameters())
print(f"Number of parameters: {total_params}")
optimizer = torch.optim.Adam(
            params=model.parameters(),
            lr=1e-4,
            weight_decay=1e-6
)
criterion = nn.CrossEntropyLoss()
mapping_N1 = list(range(N1))
for epoch in range(NUM_EPOCH):
  running_loss = 0.0
  print('Epoch ' + str(epoch+1)+ ':')
  random.shuffle(mapping_N1)
  for i in range(N1):
    optimizer.zero_grad()
    data_i = DATA_TRAIN_N1[mapping_N1[i]]
    x = torch.tensor(np.expand_dims((np.array(data_i['process'])-np.array([[50,0]]))/np.array([[50,10]]),0)).float().to(device)
    bin_mask = torch.tensor(np.array(data_i['binary mask'])).unsqueeze(0).unsqueeze(-1).float().to(device)
    output = model(x,bin_mask)
    label = torch.tensor(METHODMAPPING[data_i['label']]).unsqueeze(0).to(device)
    loss = criterion(output,label)
    loss.backward()
    optimizer.step()
    running_loss += loss.item()
    if i % 2000 == 1999:    # print every 2000 mini-batches
      print(f'[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 2000:.3f}')
      running_loss = 0.0
  num_correct = 0
  start =time.time()
  with torch.inference_mode():
    for i in range(N2):
      data_i = DATA_TRAIN_N2[i]
      x = torch.tensor(np.expand_dims((np.array(data_i['process'])-np.array([[50,0]]))/np.array([[50,10]]),0)).float().to(device)
      bin_mask = torch.tensor(np.array(data_i['binary mask'])).unsqueeze(0).unsqueeze(-1).float().to(device)
      output = model(x,bin_mask)
      predict = torch.argmax(output,dim=-1)
      label = torch.tensor(METHODMAPPING[data_i['label']]).to(device)
      if label==predict:
        num_correct+=1
  end = time.time()
  print('Val acc = ' + str(num_correct/N2))
  print(end-start)