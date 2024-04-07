from sampling import sampling_process
from standard_round_robin import constant_round_robin
from cal_quantum import *
import pandas as pd
import time
import csv

np.random.seed(int(time.time()))

with open('process_information.csv','w') as file:
    pass

METHOD_ZOO = {
    'median_burst':(median_burst,constant_round_robin),
    'average_burst':(average_burst,constant_round_robin),
    'average_max_burst':(average_max_burst,constant_round_robin),
    'sqrt_median_HB_burst':(sqrt_median_HB_burst,constant_round_robin),
    'average_median_burst':(average_median_burst,constant_round_robin),
    'sqrt_average_median_burst':(sqrt_average_median_burst,constant_round_robin),
    'average_median_max':(average_median_max,constant_round_robin),
    'sqrt_median_max':(sqrt_median_max,constant_round_robin)
}




DATA_LIST ={
    'avg_turnaround_time' : [],
    'avg_waiting_time' : [],
    'avg_response_time' : [],
    'context_swiches' : [],
    'response_time_var' : []
}



field_names =[]

Number_of_Process = 10

for i in range(Number_of_Process):
    field_names.append('P'+ str(i+1))


NUMBER_OF_DATA_POINT = 10

mydata = []

for i in range(NUMBER_OF_DATA_POINT):
    #time.sleep(0.5)
    processes,burst_time_array,arrival_time_array = sampling_process(
        np.random.randint(1,3),np.random.randint(1,2),np.random.randint(1,3),np.random.randint(0,10),Number_of_Process
    )
    new_row = dict(zip(field_names,list(zip(burst_time_array,arrival_time_array))))
    ROW = {
        'avg_turnaround_time' : new_row.copy(),
        'avg_waiting_time' : new_row.copy(),
        'avg_response_time' : new_row.copy(),
        'context_swiches' : new_row.copy(),
        'response_time_var' : new_row.copy()
    }
    for method in METHOD_ZOO:
        cal_quantum,round_robin = METHOD_ZOO[method]
        quantum_time = np.int32(cal_quantum(burst_time_array))
        avg_turnaround_time, avg_waiting_time, avg_response_time,context_swiches,response_time_var = constant_round_robin(processes,quantum_time)
        ROW['avg_turnaround_time'].update({method : avg_turnaround_time})
        ROW['avg_waiting_time'].update({method : avg_waiting_time})
        ROW['avg_response_time'].update({method : avg_response_time})
        ROW['context_swiches'].update({method : context_swiches})
        ROW['response_time_var'].update({method : response_time_var})

        new_row.update({method : (avg_turnaround_time,avg_waiting_time,avg_response_time,context_swiches,response_time_var)})
        #print(method+ ' method:')
        #print("Average Turnaround Time:", avg_turnaround_time)
        #print("Average Waiting Time:", avg_waiting_time)
        #print("Average Response Time:", avg_response_time)
        #print('Number of context switches:', context_swiches)
        mydata.append(new_row)



    #write data information
    with open('process_information.csv','a') as file:
        writer = csv.writer(file)
        writer.writerow(['Test' + str(i) +':'])
    data = {'Processes' : field_names ,'Burst time':burst_time_array , 'Arrival time':arrival_time_array}
    data = pd.DataFrame(data)
    data.to_csv('process_information.csv',mode='a',header=True,index=False)

    with open('process_information.csv','a') as file:
        writer = csv.writer(file)
        writer.writerow(['---------------------------'])

    for factor in DATA_LIST:
        DATA_LIST[factor].append(ROW[factor])


for method in METHOD_ZOO:
    field_names.append(method)





for factor in DATA_LIST:
    file_path = factor+'_'+str(Number_of_Process)+'processes' + '.csv'
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        # Write header
        writer.writeheader()
    
        # Write rows
        for row in DATA_LIST[factor]:
            writer.writerow(row)

csv_file_path = 'all.csv'

with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, field_names)
    
    # Write header
    writer.writeheader()
    
    # Write rows
    for row in mydata:
        writer.writerow(row)
