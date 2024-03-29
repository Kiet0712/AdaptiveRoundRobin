from process import Process


class ProcessScheduling(object):
    def __init__(self,arrival_time: list[float],burst_time: list[float]) -> None:
        super().__init__()
        self.arrival_time = arrival_time
        self.burst_time = burst_time
    def avg_waiting_time(self) -> float:
        raise NotImplementedError
    def avg_turn_around_time(self) -> float:
        raise NotImplementedError
    def avg_resonse_time(self) -> float:
        raise NotImplementedError
    
    
