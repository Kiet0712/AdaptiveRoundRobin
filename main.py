from sampling import sampling_process
from standard_round_robin import constant_round_robin
from cal_quantum import *
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
processes,burst_time_array,arrival_time_array = sampling_process(
    10,4,0,0,10
)
for method in METHOD_ZOO:
    cal_quantum,round_robin = METHOD_ZOO[method]
    quantum_time = cal_quantum(burst_time_array)
    avg_turnaround_time, avg_waiting_time, avg_response_time,context_swiches,var_response = round_robin(processes, quantum_time)
    print(method+ ' method:')
    print("Average Turnaround Time:", avg_turnaround_time)
    print("Average Waiting Time:", avg_waiting_time)
    print("Average Response Time:", avg_response_time)
    print("Variance Response Time:",var_response)
    print('Number of context switches:', context_swiches)