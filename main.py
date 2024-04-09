from sampling import sampling_process
from standard_round_robin import constant_round_robin
from cal_quantum import *
from plot import plot_result

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
processes,burst_time_array,arrival_time_array = sampling_process(
    100,40,20,3,10
)



plotData = {
        'Average_Turnaround': {},
        'Average_Waiting': {},
        'Average_Response': {},
        'Variance_Response': {},
        'Number_of_context_switches': {}
    }

for method in METHOD_ZOO:
    cal_quantum,round_robin = METHOD_ZOO[method]
    quantum_time = np.int32(cal_quantum(burst_time_array))
    avg_turnaround_time, avg_waiting_time, avg_response_time, context_switches, var_response = round_robin(processes, quantum_time)
    print(method+ ' method:')
    print("Average Turnaround Time:", avg_turnaround_time)
    print("Average Waiting Time:", avg_waiting_time)
    print("Average Response Time:", avg_response_time)
    print("Variance Response Time:",var_response)
    print('Number of context switches:', context_switches)

    plotData['Average_Turnaround'][method] = avg_turnaround_time
    plotData['Average_Waiting'][method] = avg_waiting_time
    plotData['Average_Response'][method] = avg_response_time
    plotData['Variance_Response'][method] = var_response
    plotData['Number_of_context_switches'][method] = context_switches

plot_result(plotData)