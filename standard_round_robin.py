def constant_round_robin(processes, time_quantum):
    ready_queue = []  # Queue to hold ready processes
    turnaround_time = [0] * len(processes)  # Time from submission to completion
    waiting_time = [0] * len(processes)  # Time spent waiting in ready queue
    response_time = [0] * len(processes)  # Time from submission to first CPU allocation
    context_switches = 0  # Number of context switches
    current_time = 0   # Current time
    completed = 0     # Number of completed processes

    # Add processes to ready queue based on arrival time
    ready_queue = sorted(processes, key=lambda p: (p[1],p[2]))  # Sort by arrival time
    while completed != len(processes):
        if not ready_queue:
            current_time += 1  # Idle time if no processes are ready
            continue

        current_process = ready_queue.pop(0)
        process_id, arrival_time, burst_time = current_process

        # Calculate response time for the first time a process enters the queue
        if response_time[process_id] == 0:
            response_time[process_id] = current_time - arrival_time

        if burst_time <= time_quantum:
            # Process can finish within time quantum
            current_time += burst_time
            turnaround_time[process_id] = current_time - arrival_time
            waiting_time[process_id] = turnaround_time[process_id] - burst_time
            completed += 1
        else:
            # Process needs more time
            burst_time -= time_quantum
            current_time += time_quantum
            ready_queue.append((process_id, arrival_time, burst_time))

        # Count context switch unless it's the last process
        if completed != len(processes):
            context_switches += 1

    # Calculate average turnaround, waiting, and response times
    avg_turnaround_time = sum(turnaround_time) / len(processes)
    avg_waiting_time = sum(waiting_time) / len(processes)
    avg_response_time = sum(response_time) / len(processes)

    return avg_turnaround_time, avg_waiting_time, avg_response_time, context_switches

if __name__ == "__main__":
    import random
    import matplotlib.pyplot as plt
    ans = [[],[],[],[]]
    random.seed(123)
    processes = []
    MIN_BURST_TIME = 1_000
    MAX_BURST_TIME = 100_000
    for i in range(100):
        processes.append((i, 0, random.randint(MIN_BURST_TIME, MAX_BURST_TIME)))
    for i in range(MIN_BURST_TIME, MAX_BURST_TIME+1, 100):
        x = constant_round_robin(
            processes,
            i
        )
        ans[0].append(x[0])
        ans[1].append(x[1])
        ans[2].append(x[2])
        ans[3].append(x[3])

    fig, axes = plt.subplots(2, 2) 
    axes[0, 0].plot(ans[0], color='red')
    axes[0, 0].title.set_text('Turnaround')
    axes[0, 1].plot(ans[1], color='green')
    axes[0, 1].title.set_text('Waiting')
    axes[1, 0].plot(ans[2], color='blue')
    axes[1, 0].title.set_text('Response')
    axes[1, 1].plot(ans[3], color='orange')
    axes[1, 1].title.set_text('Context switch')
    plt.show()