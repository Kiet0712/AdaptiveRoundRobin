from sampling import sampling_process
from standard_round_robin import constant_round_robin
from cal_quantum import *
import matplotlib.pyplot as plt
METHOD_ZOO = {
    'median':(median_burst,constant_round_robin),
    'average':(average_burst,constant_round_robin),
    'average_max':(average_max_burst,constant_round_robin),
    'sqrt\nmedian_HB':(sqrt_median_HB_burst,constant_round_robin),
    'average\nmedian':(average_median_burst,constant_round_robin),
    'sqrt_average\nmedian':(sqrt_average_median_burst,constant_round_robin),
    'average\nmedian_max':(average_median_max,constant_round_robin),
    'sqrt\nmedian_max':(sqrt_median_max,constant_round_robin)
}
processes,burst_time_array,arrival_time_array = sampling_process(
    10,4,0,0,10
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
    quantum_time = cal_quantum(burst_time_array)
    avg_turnaround_time, avg_waiting_time, avg_response_time,context_swiches,var_response = round_robin(processes, quantum_time)
    print(method+ ' method:')
    print("Average Turnaround Time:", avg_turnaround_time)
    print("Average Waiting Time:", avg_waiting_time)
    print("Average Response Time:", avg_response_time)
    print("Variance Response Time:",var_response)
    print('Number of context switches:', context_swiches)

    plotData['Average_Turnaround'][method] = avg_turnaround_time
    plotData['Average_Waiting'][method] = avg_waiting_time
    plotData['Average_Response'][method] = avg_response_time
    plotData['Variance_Response'][method] = var_response
    plotData['Number_of_context_switches'][method] = context_swiches


fig, axes = plt.subplots(5, 1)
i = 0
for metric in plotData:
    #axes[i].set_xticks(range(len(plotData[metric].keys())), plotData[metric].keys(), rotation=90)
    #axes[i].bar(range(len(plotData[metric].keys())), plotData[metric].values())
    axes[i].bar(range(len(plotData[metric].keys())), plotData[metric].values())
    axes[i].title.set_text(metric)
    if i==4:
        break
    axes[i].tick_params(
            axis='x',          # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            bottom=False,      # ticks along the bottom edge are off
            top=False,         # ticks along the top edge are off
            labelbottom=False
        ) 
    i += 1  
axes[4].set_xticks(range(len(plotData[metric].keys())), plotData[metric].keys(), rotation=90)
plt.show()