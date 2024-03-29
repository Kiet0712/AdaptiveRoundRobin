class Process(object):
    def __init__(self,burst_time: float) -> None:
        super().__init__()
        self.burst_time = burst_time
        self.remaining_time = burst_time
    def __call__(self,execution_time: float):
        if execution_time>=self.remaining_time:
            current_remaining_time = self.remaining_time
            self.remaining_time=0
            return True,execution_time-current_remaining_time
        else:
            self.remaining_time -= execution_time
            return False,0

