import matplotlib.pyplot as plt

def plot_result(plotData=None):
    '''
    Args:
        plotData: A dict of dict.
            plotData = {
                'Average_Turnaround': {'foo': 1234, 'bar': 12345},
                'Average_Waiting': {'foo': 1234, 'bar': 12345},
                'Average_Response': {'foo': 1234, 'bar': 12345},
                'Variance_Response': {'foo': 1234, 'bar': 12345},
                'Number_of_context_switches': {'foo': 1234, 'bar': 12345}
            }
    '''
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

if __name__ == "__main__":
    plot_result({
                'Average_Turnaround': {'foo': 1234, 'bar': 12345},
                'Average_Waiting': {'foo': 1234, 'bar': 12345},
                'Average_Response': {'foo': 1234, 'bar': 12345},
                'Variance_Response': {'foo': 1234, 'bar': 12345},
                'Number_of_context_switches': {'foo': 1234, 'bar': 12345}
            })